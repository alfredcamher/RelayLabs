#!/usr/bin/env python3
"""
CEO Autónomo - Load Testing Script
Tests server performance under concurrent requests

Usage: python load-test.py --url https://yourdomain.com --requests 100
"""

import argparse
import asyncio
import aiohttp
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


class LoadTester:
    """Simple load tester."""
    
    def __init__(self, base_url, concurrency=10, total_requests=100):
        self.base_url = base_url.rstrip('/')
        self.concurrency = concurrency
        self.total_requests = total_requests
        self.results = {
            'success': 0,
            'failed': 0,
            'times': [],
            'errors': []
        }
    
    async def test_health(self, session, request_id):
        """Test health endpoint."""
        start = time.time()
        try:
            async with session.get(f"{self.base_url}/health", timeout=5) as resp:
                elapsed = time.time() - start
                if resp.status == 200:
                    self.results['success'] += 1
                    self.results['times'].append(elapsed)
                    return True
                else:
                    self.results['failed'] += 1
                    self.results['errors'].append(f"HTTP {resp.status}")
                    return False
        except Exception as e:
            self.results['failed'] += 1
            self.results['errors'].append(str(e))
            return False
    
    async def run_load_test(self):
        """Run load test with concurrency."""
        print(f"Starting load test...")
        print(f"  URL: {self.base_url}/health")
        print(f"  Requests: {self.total_requests}")
        print(f"  Concurrency: {self.concurrency}")
        print()
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(self.total_requests):
                task = self.test_health(session, i)
                tasks.append(task)
            
            # Run with semaphore for concurrency control
            semaphore = asyncio.Semaphore(self.concurrency)
            
            async def sem_task(task):
                async with semaphore:
                    return await task
            
            await asyncio.gather(*[sem_task(t) for t in tasks])
    
    def report(self):
        """Generate report."""
        print("\n" + "=" * 50)
        print("LOAD TEST RESULTS")
        print("=" * 50)
        print(f"Total requests: {self.total_requests}")
        print(f"Successful: {self.results['success']}")
        print(f"Failed: {self.results['failed']}")
        
        if self.results['times']:
            times = self.results['times']
            print(f"\nLatency:")
            print(f"  Min: {min(times):.3f}s")
            print(f"  Max: {max(times):.3f}s")
            print(f"  Avg: {sum(times)/len(times):.3f}s")
            
            # Calculate p95
            sorted_times = sorted(times)
            p95_idx = int(len(sorted_times) * 0.95)
            p95 = sorted_times[min(p95_idx, len(sorted_times)-1)]
            print(f"  P95: {p95:.3f}s")
        
        print(f"\nThroughput: {self.results['success'] / (sum(self.results['times']) + 0.001):.1f} req/s")
        
        if self.results['failed'] > 0:
            print(f"\nErrors:")
            for err in set(self.results['errors'][:5]):
                print(f"  - {err}")
        
        print("=" * 50)
        
        success_rate = self.results['success'] / self.total_requests * 100
        return success_rate >= 95


def main():
    parser = argparse.ArgumentParser(description='Load test CEO Autónomo server')
    parser.add_argument('--url', default='http://localhost:4242', help='Base URL')
    parser.add_argument('-c', '--concurrency', type=int, default=10, help='Concurrent requests')
    parser.add_argument('-n', '--requests', type=int, default=100, help='Total requests')
    args = parser.parse_args()
    
    print(f"CEO Autónomo - Load Test")
    print(f"Started: {datetime.now().isoformat()}")
    
    tester = LoadTester(args.url, args.concurrency, args.requests)
    asyncio.run(tester.run_load_test())
    success = tester.report()
    
    return 0 if success else 1


if __name__ == '__main__':
    import sys
    sys.exit(main())