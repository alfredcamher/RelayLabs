# CEO Autónomo - Launch Playbook
## Pre-Flight Checklist & Go/No-Go Decision

**Document Version:** 1.0.0  
**Last Updated:** 2026-04-02  
**Launch Target:** TBD (Fill in before launch)

---

## Phase 1: Pre-Launch (T-7 Days)

### Infrastructure Setup
- [ ] Stripe account created and verified
- [ ] Product created: "CEO Autónomo Guide" - $47 USD
- [ ] Price ID copied to `.env` file
- [ ] Stripe webhook endpoint configured (Production URL)
- [ ] Webhook secret copied to `.env` file
- [ ] Email provider account created (SendGrid recommended)
- [ ] Email API key copied to `.env` file
- [ ] `FROM_EMAIL` configured and verified

### Domain & Hosting
- [ ] Domain purchased/configured
- [ ] Domain pointed to hosting (A records or CNAME)
- [ ] SSL certificate active (Let's Encrypt or provider)
- [ ] Environment variables set on hosting platform
- [ ] Health check passes: `curl https://yourdomain.com/health`

### Content
- [ ] PDF generated: `CEO-Autonomo-Guide.pdf` (41 pages verified)
- [ ] PDF uploaded to CDN (S3/CloudFront or similar)
- [ ] Download URL tested (incognito browser)
- [ ] File size optimized (< 10MB for fast download)

### Analytics
- [ ] Google Analytics 4 configured
- [ ] Conversion events set up
- [ ] Stripe Dashboard bookmarked for tracking
- [ ] UTM parameters planned for social links

---

## Phase 2: Testing (T-3 Days)

### Run Test Suite
```bash
# From /payment directory
./test-checkout.sh
```

**Expected Output:**
- All checks pass ✅
- Server starts on localhost:4242
- Checkout creates session successfully
- Webhook receives events

### End-to-End Test (Manual)
1. **Test Payment (Success):**
   - Card: `4242 4242 4242 4242`
   - Any future date, any CVC, any ZIP
   - Email: Use your email
   - Verify receipt and download

2. **Test Decline:**
   - Card: `4000 0000 0000 0002`
   - Verify graceful error handling

3. **Test 3D Secure:**
   - Card: `4000 0027 6000 3184`
   - Authenticate and complete
   - Verify webhook fires

4. **Test Cancel:**
   - Start checkout, click back
   - Verify redirect to cancel page

5. **Test Webhook Delivery:**
   - Complete successful purchase
   - Check `purchases.log` for entry
   - Verify email received
   - Check Stripe Dashboard for event

### Mobile Testing
- [ ] iOS Safari (test purchase flow)
- [ ] Android Chrome (test purchase flow)
- [ ] iPad/tablet responsive check

### Cross-Browser Testing
- [ ] Chrome Desktop
- [ ] Firefox Desktop
- [ ] Safari Desktop

**Verify for each:**
- Checkout button visible and functional
- Stripe checkout loads
- Success page displays
- Download link works

---

## Phase 3: Content Finalization (T-2 Days)

### Marketing Assets Review
- [ ] Landing page copy: Final grammar check
- [ ] Twitter thread: Scheduled in Buffer/TweetDeck
- [ ] Email sequence: Sent test to yourself
- [ ] Launch checklist: All items reviewed

### Social Media
- [ ] Twitter bio updated with link
- [ ] LinkedIn post drafted
- [ ] Instagram/Facebook if applicable
- [ ] Profile pic/banner updated if needed

### Support Systems
- [ ] Dedicated email: support@yourdomain.com
- [ ] FAQ prepared (Top 5 questions)
- [ ] Refund policy documented
- [ ] Response time commitment (e.g., 24 hours)

---

## Phase 4: Go/No-Go Decision (T-1 Day)

### Go Criteria (ALL must be green)
| Criterion | Status | Notes |
|-----------|--------|-------|
| Stripe webhook receiving events | [ ] | Test payment triggered event |
| Email delivery working | [ ] | Received test email |
| Download link accessible | [ ] | Tested in incognito |
| Health check responds 200 | [ ] | curl https://domain/health |
| Mobile purchase works | [ ] | Tested on iOS/Android |
| PDF quality verified | [ ] | 41 pages, all content correct |

**Go/No-Go Decision:** ___________
**Decision Maker:** ___________
**Date:** ___________

### If NO-GO:
1. Document blockers
2. Set new target date
3. Fix issues within 48 hours

---

## Phase 5: Launch Day (T-0)

### Morning Routine (2 Hours Before)
- [ ] Wake up early, funds coffee ☕
- [ ] Final health check
- [ ] Verify analytics tracking active
- [ ] Test one more purchase flow

### Launch Sequence
**T-0: Announcement Post**
```
Platform: Twitter
Time: [Your optimal time]
Content: Opening tweet of thread
Link: [Your checkout URL with UTM]
```

**T+15min: Engagement**
- Monitor replies to launch post
- Reply to comments/questions
- Retweet/quote tweet from supportive followers

**T+1hr: LinkedIn Cross-Post**
- Adapt Twitter thread for LinkedIn format
- Include personal story element
- Tag relevant connections

**T+2hrs: Email List**
- Send to existing list (if applicable)
- Subject: "It's here: CEO Autónomo Guide"
- Include direct purchase link

**T+4hrs: Follow-up**
- Post follow-up tweet: "3 hours in..."
- Share early social proof if any
- Answer DMs/replies

**T+24hrs: Day 1 Wrap**
- Screenshot Stripe dashboard
- Organic thank-you post
- Plan Day 2 content

---

## Phase 6: Post-Launch (Days 2-7)

### Daily Tasks
- [ ] Check Stripe for new purchases
- [ ] Email delivery confirmation (purchases.log)
- [ ] Reply to customer emails within 24h
- [ ] Monitor social mentions
- [ ] Update analytics tracking

### Day 2
- [ ] "First 24 hours" recap post
- [ ] Share any early testimonials
- [ ] Address any technical issues

### Day 3-4
- [ ] Framework teardown tweet (educational)
- [ ] "Behind the scenes" content
- [ ] Answer common questions publicly

### Day 5-7
- [ ] Case study/promise fulfilled content
- [ ] Soft ask: Reviews and referrals
- [ ] Tease future content/product

---

## Metrics Dashboard

### Primary KPIs
| Metric | Target | Day 1 | Day 7 | Day 30 |
|--------|--------|-------|-------|--------|
| Visitors to checkout | N/A | | | |
| Checkout initiations | | | | |
| Completed purchases | 10+ | | | |
| Conversion rate | >2% | | | |
| Revenue | $470+ | | | |
| Email delivery rate | >95% | | | |

### Secondary Metrics
- Social engagement (likes, retweets)
- Email open rate (if email blast sent)
- Refund requests (target: <5%)
- Support inquiries (target: <10)

---

## Emergency Procedures

### Payment Processing Down
1. Check Stripe status: https://status.stripe.com
2. Verify webhook endpoint responding
3. Check hosting platform status
4. Have backup: Disable checkout, collect emails

### Email Delivery Failing
1. Check SendGrid/AWS SES status
2. Verify API key valid
3. Switch to manual delivery mode
4. Send emails manually from purchased log

### PDF Download Broken
1. Verify CDN URL accessible
2. Check file permissions
3. Have backup download method ready
4. Email PDF directly if needed

### High Refund Rate
1. Review negative feedback
2. Analyze common complaints
3. Consider product update
4. Pause marketing if >10%

---

## Quick Reference

### Important URLs
- Stripe Dashboard: https://dashboard.stripe.com
- SendGrid Dashboard: https://app.sendgrid.com
- Health Check: https://yourdomain.com/health
- Checkout: https://yourdomain.com

### Test Cards
```
Success: 4242 4242 4242 4242
Decline: 4000 0000 0000 0002
3D Auth: 4000 0027 6000 3184
```

### Support Response Templates

**General Support:**
"Thanks for reaching out! I'll get back to you within 24 hours. - Alfred"

**Technical Issue:**
"Thanks for reporting this. Can you share a screenshot of what you're seeing? I'll investigate immediately."

**Refund Request:**
"No problem at all. I want this to be valuable for you. Processing your refund now — you should see it in 5-10 business days."

---

## Post-Mortem Template

**Complete 7 days after launch:**

### What Went Well?
1. 
2. 
3. 

### What Could Improve?
1. 
2. 
3. 

### Lessons Learned?
- 

### Next Launch Changes?
- 

### Revenue Summary
- Total sales: 
- Total refunds: 
- Net