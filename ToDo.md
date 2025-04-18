## continued tasks

**add comments** 

- necessary for all code-files (include examples) 
- other project-partners need to learn from that code and will appreciate any help

**watchdog for email-account**

- to retrieve all DTVP-related mails and check for specific client-bids
- extract URL for DTVP

- it's possible to create an MS Developer-Account to get a Azure test-tenant and test the app with Exchange Online
    - get access [here](https://learn.microsoft.com/de-de/office/developer-program/microsoft-365-developer-program)
    - register your app [more info](https://helpcenter.veeam.com/docs/vdcm365/userguide/check_perms_for_o365_exchange_api.html)
    - folloow [that example](https://www.youtube.com/watch?app=desktop&v=bBslvqBCjAA&t=0s&ab_channel=SigmaCoding)

## start triggered by receiving a specific email

**login to DTVP with URL**
- download the whole documents-package as ZIP

**tasks already implemented as PoC**

- extract ZIP
- split documents & create embeddings
- feed the LLM with that embeddings
- see [How to create a vactor-db for use with an LLM](https://github.com/pixegami)

**prepare first bid-tasks**

- check for project-name from documents by LLM (or from DTVP)
    - create Ensemble / Sharepoint folder respecting naming-conventions (date is submission-date)
        - YYYY.MM.DD - {project-name}
    - upload all documents

- create ESR-A slides (based on Bundesbank-Template)
    - Update project-name on all slides
    - Update timeline, deal-qualification and details, OMF-category and TCV, stakeholder
    - store slides on Ensemble / Sharepoint
    - see [How to manipulate PPTX-slides with an LLM](https://medium.com/@matteo28/how-to-generate-a-powerpoint-with-an-llm-3b0448a48125)

- Create ESR-A call and send slides to OMF-approver (plus stakeholder)
    - ESR-A as soon as possible
    - automatically check calendar of all OMF-approvers (and stakeholders) to find a suitable slot
    - create a MS Teams Call with details about the bids
    - see [How to invite for MS Teams call with Exchange Online](https://learn.microsoft.com/en-us/answers/questions/1328906/how-to-create-a-meetings-call-using-graph-api-in-p)

## After positive ESR-A and handing over to OPL

- Prepare ESR-B and ESR-C slides
    - store slides on Ensemble / Sharepoint
    - see [How to manipulate PPTX-slides with an LLM](https://medium.com/@matteo28/how-to-generate-a-powerpoint-with-an-llm-3b0448a48125)
- create CRM-opportunity
    - check for API
- create Talento-opportunity to receive profile-references
    - check for API
- create DRSR-request
    - check for API
- invite for ESR-B, ESR-C, SSR-Solution, SSR-Finance and SSR-Legal
    - see [How to invite for MS Teams call with Exchange Online](https://learn.microsoft.com/en-us/answers/questions/1328906/how-to-create-a-meetings-call-using-graph-api-in-p)
- search for project-references in BidGen and BDKX
- automatically match received CV to project-roles and/or seniority
- check for necessary concept to submit
    - decide for possible web-sources
    - embed sources
    - create concepts and send it for review to stakeholder and experts (profile-references)
- regulary remind the OPL to necessary CRM-action (stage-processing)
    - by MS Teams chat-messages