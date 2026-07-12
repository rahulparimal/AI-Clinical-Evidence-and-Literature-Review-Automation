# Configuration

## NCBI
Register `tool` and `email`, use an API key for higher supported request rates, batch retrieval, cache responses, and comply with NCBI copyright and usage requirements.

## Search index fields
`projectId`, `protocolId`, `source`, `sourceRecordId`, `title`, `abstract`, `publicationDate`, `authors`, `doi`, `pmid`, `device`, `analyte`, `studyType`, `screeningStatus`, `appraisalStatus`, `acl`, `contentVector`, `contentHash`.

## Production controls
- Private endpoints and disabled public access.
- Managed identity rather than stored service keys.
- Key Vault references for unavoidable secrets.
- Durable queues for ingestion and extraction.
- Rate limiting and backoff for external literature sources.
- Retain exact query, date, database, result count, and imported identifier set.
