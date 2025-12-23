#### 9.1.1 Metadata System Functionality

**User Story:**
As a **site owner** I want **each page to have accurate metadata** so that **s**earch engines and social platforms display the correct information for my portfolio**.

**What Was Tested:**
I tested that every page in my portfolio correctly displays dynamic titles, meta descriptions, and OpenGraph metadata. I checked the homepage, About page, Projects page, CV page, Contact page, Blog list, and Blog detail pages to confirm each one outputs the right metadata in the page source. This includes checking the `<title>` tag, the meta description, and all OG tags. 

**Acceptance Criteria:**
[x] `<title>` dynamically updates per page  
[x] Meta descriptions display the correct per-page content  
[x] OG titles render correctly  
[x] OG descriptions render correctly  
[x] OG image loads from Cloudinary  
[x] OG URL is correct for each page  
[x] Metadata appears correctly in the rendered HTML source  
[x] No duplicate `<title>` tags appear

**Tasks Completed:**
[x] Added dynamic title blocks to all templates  
[x] Added dynamic `meta_description` blocks to all templates by inspecting each page in Dev Tools making sure they appeared  
[x] Implemented page-specific OpenGraph blocks  
[x] Updated OG URL to use `request.path` where needed
[x] Replaced placeholder OG fields in blog_detail  
[x] Removed duplicate `<title>` from `base.html`  
[x] Validated metadata through WhatsApp and [Facebook's Sharing Debugger](https://developers.facebook.com/tools/debug/) and [LinkedIn Inspector](https://www.linkedin.com/post-inspector/)

**Notes:**
This feature relied on correctly structuring the `<head>` section for every template. I had to fix a missing title in the blog detail OG block and ensure the OG URL was dynamic instead of hard-coded. I also discovered a duplicate `<title>` tag in the base template, which caused inconsistent browser tab titles until removed. After deploying, Cloudflare caching sometimes held old metadata, so purging the cache was necessary before testing. The final result is a clean, dynamic metadata system across all pages.

--

#### 9.1.2 Structured Data (Schema.org) Implementation

**User Story:**
As a **site owner** I want **structured data added to every page** so that **Google can understand my content and improve how my pages appear in search results**.

**What Was Tested:**
I tested that each page outputs valid JSON-LD structured data using the correct schema types. The homepage uses WebPage, the About page uses AboutPage, the Projects page uses CollectionPage, the CV page uses AboutPage, the Contact page uses ContactPage, the Blog list uses CollectionPage, and each blog post uses BlogPosting. I checked that dates, URLs, titles, descriptions, and author fields were all correct. I confirmed validity using [Rich Test Results Test](https://search.google.com/test/rich-results). 

**Acceptance Criteria:**
[x] Every page outputs one JSON-LD block  
[x] JSON-LD validates in Google’s Rich Results Test  
[x] Correct schema types used (WebPage, AboutPage, CollectionPage, ContactPage, BlogPosting)  
[x] Blog posts show **Article** as a valid rich-result item  
[x] All URLs match the live site  
[x] Author data appears correctly on all pages  
[x] Publish and modified dates appear correctly for blog posts  
[x] No critical errors in any structured data test

**Tasks Completed:**
[x] Added a `structured_data` block to `base.html`  
[x] Implemented schema for all main pages  
[x] Implemented dynamic BlogPosting schema for blog detail pages  
[x] Added headline, excerpt, dates, and URLs dynamically  
[x] Validated each page in Google’s *Rich Results Test*  
[x] Ensured JSON-LD escaped variables correctly (`escapejs`)  
[x] Fixed OG/schema alignment on blog detail view  
[x] Purged *Cloudflare* cache when old structured data was cached

**Notes:**
The *Rich Results Test* confirmed that the BlogPosting schema successfully qualifies as an Article rich result. The main challenge was ensuring that dynamic values (title, description, timestamps, slugs, and URLs) were correctly escaped for JSON. Blog detail pages required special attention because Google is strict about Article schema. After the schema changes were deployed, Cloudflare initially cached old responses, so purging the cache was necessary before retesting. Once refreshed, every page validated successfully.

---

#### 1.1.1 Canonical URL Implementation

**User Story:**  
As a **site owner** I want **each page to declare a single authoritative URL** so that **search engines do not mistake alternate URLs, parameters, or browser variations for duplicate content**.

**What Was Tested:**  
I checked that every page in my portfolio correctly outputs a `<link rel="canonical">` tag based on the actual page being viewed. I confirmed that the canonical tag appears in the raw HTML source (not Dev Tools), that it uses the proper HTTPS domain, that it includes the correct page path, and that it contains no query parameters or tracking strings. This ensures that each page presents one stable, official URL.  

**Acceptance Criteria:**  
[x] The canonical tag appears exactly once in the `<head>` of each rendered page  
[x] The canonical URL uses the correct domain (`https://axdeklerk.co.uk/`)  
[x] The canonical URL includes the correct page path (e.g., `/cv/`)  
[x] No query parameters or tracking strings appear in the canonical URL  
[x] The canonical tag is generated dynamically using `request.build_absolute_uri`  
[x] The tag remains consistent across all pages regardless of how the URL was reached (e.g., with or without trailing slash)

**Tasks Completed:**  
[x] Added a canonical block to `base.html` using `request.build_absolute_uri`  
[x] Rendered a live page and opened the raw HTML source  
[x] Searched for the `<link rel="canonical">` tag in the source  
[x] Verified that the canonical URL was correct, clean, and dynamic  
[x] Confirmed that the update applies to all templates inheriting from the

**Notes:**  
I learned that duplicate URLs often occur automatically due to browser behaviour, social media link parameters, trailing slashes, HTTP/HTTPS variations, and user input. Adding a dynamic canonical tag ensures that Google always sees a single authoritative URL for each page, which prevents SEO dilution and improves the professional quality of the site. The test confirmed that the implementation works exactly as intended.

---

#### 9.5.3 Static Manifest & Favicon Pipeline

**User Story:**  
As a **site owner**, I want **my site’s favicon, * icon, and manifest file to load correctly in production** so that **my portfolio feels polished, professional, and behaves correctly across browsers and devices**.

**What Was Tested:**  
I tested whether all static icon assets (*, ICO, *) and the `manifest.json` file were being correctly collected, deployed, and served in production on **Heroku**. This testing ensured that all branding files existed in the deployed `/static/` directory and were accessible to users. 

**Acceptance Criteria:**  
[x] All icons load from `/static/icons/`  
[x] `favicon.ico` loads in the browser tab  
[x] * icon loads at `/static/icons/ax_icon.*`  
[x] `manifest.json` loads from `/static/manifest.json`  
[x] **Django** collects all static files during deployment  
[x] **Heroku** deploy includes the manifest file  
[x] No 404s for favicon, * icons, or manifest  
[x] `.gitignore` no longer blocks required files  

**Tasks Completed:**  
[x] Verified all static settings in **Django**  
[x] Confirmed **Whitenoise** was active and correctly ordered  
[x] Checked `/static/` behaviour directly in logs  
[x] Investigated why only JSON-based files were missing  
[x] Located the `.gitignore` rule causing the issue (`*.json`)  
[x] Removed the rule   
[x] Force-added `manifest.json` to *Git* using `git add -f`  
[x] Redeployed to **Heroku** and let collectstatic rebuild  
[x] Retested all icon and manifest routes successfully  

**Notes:**  
This issue turned out to be caused by a blanket `.gitignore` rule that ignored **every** `.json` file in the project, including the critical `manifest.json` used by browsers and *PWAs*. Although all *PNG*, *ICO*, *SVG*, and *CSS* files deployed correctly, the manifest was never tracked by *Git* and therefore never included in **Heroku**’s slug. Once I corrected the `.gitignore` entry and force-added the manifest file, `collectstatic` picked it up and the file appeared correctly under `/static/`. This was a good reminder that *Git* ignore rules can silently break production even when the **Django** static pipeline is working perfectly.


## 9.6 Lighthouse

#### 9.6.3 HTTPS and Mixed Content Validation (Lighthouse Audit)

**User Story**  
As a **site owner**, I want to **ensure all pages and assets are served securely over HTTPS**, so that **the site meets modern security standards and passes automated best-practice audits**.

**What Was Tested**  
The deployed site was tested using **Lighthouse** to verify that all pages load securely over `HTTPS` and do not request any insecure (HTTP) resources, particularly media assets served via **Cloudinary**.

**Acceptance Criteria**  
- [x] The site loads over `HTTPS` on all public pages  
- [x] No mixed content (HTTP resources on HTTPS pages) is detected  
- [x] **Lighthouse** does not report “Does not use HTTPS” warnings  
- [x] Media assets load correctly without browser security warnings  

**Tasks Completed**  
- [x] Ran **Lighthouse** audit on the live site after deployment  
- [x] Reviewed Best Practices and Security sections of the report  
- [x] Confirmed all media requests resolve over `HTTPS`  
- [x] Re-ran **Lighthouse** after configuration changes to confirm fix  

**Notes**  
**Lighthouse** initially flagged a mixed content issue where image assets served from **Cloudinary** were generated as `HTTP URL`s and automatically upgraded by the browser. After updating the **Cloudinary** configuration to explicitly enforce secure `URL` generation and redeploying to **Heroku**, the issue was resolved. A subsequent **Lighthouse** audit confirmed that no insecure requests remained and the Best Practices score returned to 100.
