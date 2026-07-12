param location string = resourceGroup().location
param prefix string = 'ivdevidence'
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = {name: take('${prefix}${uniqueString(resourceGroup().id)}',24) location:location sku:{name:'Standard_GRS'} kind:'StorageV2' properties:{minimumTlsVersion:'TLS1_2' allowBlobPublicAccess:false publicNetworkAccess:'Disabled'}}
resource search 'Microsoft.Search/searchServices@2023-11-01' = {name:'${prefix}-search' location:location sku:{name:'standard'} properties:{publicNetworkAccess:'disabled' hostingMode:'default'}}
resource openai 'Microsoft.CognitiveServices/accounts@2023-05-01' = {name:'${prefix}-openai' location:location kind:'OpenAI' sku:{name:'S0'} properties:{customSubDomainName:'${prefix}-${uniqueString(resourceGroup().id)}' publicNetworkAccess:'Disabled'}}
