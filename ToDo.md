## continued tasks

**watchdog for email-account**

- to retrieve all DTVP-related mails and check for specific client-bids
- extract URL for DTVP

## start triggered by receiving a specific email

**login to DTVP with URL**
- download the whole documents-package as ZIP

**tasks already implemented as PoC**

- extract ZIP
- split documents & create embeddings
- feed the LLM with that embeddings

**prepare first bid-tasks**

- check for project-name from documents by LLM (or from DTVP)
    - create Ensemble / Sharepoint folder respecting naming-conventions (date is submission-date)
        - YYYY.MM.DD - {project-name}
    - upload all documents

- create ESR-A slides (based on Bundesbank-Template)
    - Update project-name on all slides
    - Update timeline, deal-qualification and details, OMF-category and TCV, stakeholder
    - store slides on Ensemble / Sharepoint

- Create ESR-A call and send slides to OMF-approver (plus stakeholder)
    - ESR-A as soon as possible
    - automatically check calendar of all OMF-approvers (and stakeholders) to find a suitable slot
    - create a MS Teams Call with details about the bids

## After positive ESR-A and handing over to OPL

- Prepare ESR-B and ESR-C slides
    - store slides on Ensemble / Sharepoint

- create CRM-opportunity
- create Talento-opportunity to receive profile-references
- create DRSR-request
- invite for ESR-B, ESR-C, SSR-Solution, SSR-Finance and SSR-Legal
- search for project-references in BidGen and BDKX
- automatically match received CV to project-roles and/or seniority
- check for necessary concept to submit
    - create concepts and send it for review to stakeholder and experts (profile-references)
- regulary remind the OPL to necessary CRM-action (stage-processing)