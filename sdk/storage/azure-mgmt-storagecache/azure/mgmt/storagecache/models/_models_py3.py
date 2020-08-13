# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class ApiOperation(Model):
    """REST API operation description: see
    https://github.com/Azure/azure-rest-api-specs/blob/master/documentation/openapi-authoring-automated-guidelines.md#r3023-operationsapiimplementation.

    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.storagecache.models.ApiOperationDisplay
    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    """

    _attribute_map = {
        'display': {'key': 'display', 'type': 'ApiOperationDisplay'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, display=None, name: str=None, **kwargs) -> None:
        super(ApiOperation, self).__init__(**kwargs)
        self.display = display
        self.name = name


class ApiOperationDisplay(Model):
    """The object that represents the operation.

    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param provider: Service provider: Microsoft.StorageCache
    :type provider: str
    :param resource: Resource on which the operation is performed: Cache, etc.
    :type resource: str
    """

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(self, *, operation: str=None, provider: str=None, resource: str=None, **kwargs) -> None:
        super(ApiOperationDisplay, self).__init__(**kwargs)
        self.operation = operation
        self.provider = provider
        self.resource = resource


class AscOperation(Model):
    """The status of operation.

    :param id: The operation Id.
    :type id: str
    :param name: The operation name.
    :type name: str
    :param start_time: The start time of the operation.
    :type start_time: str
    :param end_time: The end time of the operation.
    :type end_time: str
    :param status: The status of the operation.
    :type status: str
    :param error: The error detail of the operation if any.
    :type error: ~azure.mgmt.storagecache.models.ErrorResponse
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'end_time': {'key': 'endTime', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'ErrorResponse'},
    }

    def __init__(self, *, id: str=None, name: str=None, start_time: str=None, end_time: str=None, status: str=None, error=None, **kwargs) -> None:
        super(AscOperation, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.error = error


class Cache(Model):
    """A Cache instance. Follows Azure Resource Manager standards:
    https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/resource-api-reference.md.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param tags: ARM tags as name/value pairs.
    :type tags: object
    :ivar id: Resource ID of the Cache.
    :vartype id: str
    :param location: Region name string.
    :type location: str
    :ivar name: Name of Cache.
    :vartype name: str
    :ivar type: Type of the Cache; Microsoft.StorageCache/Cache
    :vartype type: str
    :param identity: The identity of the cache, if configured.
    :type identity: ~azure.mgmt.storagecache.models.CacheIdentity
    :param cache_size_gb: The size of this Cache, in GB.
    :type cache_size_gb: int
    :ivar health: Health of the Cache.
    :vartype health: ~azure.mgmt.storagecache.models.CacheHealth
    :ivar mount_addresses: Array of IP addresses that can be used by clients
     mounting this Cache.
    :vartype mount_addresses: list[str]
    :param provisioning_state: ARM provisioning state, see
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property.
     Possible values include: 'Succeeded', 'Failed', 'Cancelled', 'Creating',
     'Deleting', 'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.storagecache.models.ProvisioningStateType
    :param subnet: Subnet used for the Cache.
    :type subnet: str
    :param upgrade_status: Upgrade status of the Cache.
    :type upgrade_status: ~azure.mgmt.storagecache.models.CacheUpgradeStatus
    :param network_settings: Specifies network settings of the cache.
    :type network_settings:
     ~azure.mgmt.storagecache.models.CacheNetworkSettings
    :param encryption_settings: Specifies encryption settings of the cache.
    :type encryption_settings:
     ~azure.mgmt.storagecache.models.CacheEncryptionSettings
    :param security_settings: Specifies security settings of the cache.
    :type security_settings:
     ~azure.mgmt.storagecache.models.CacheSecuritySettings
    :param sku: SKU for the Cache.
    :type sku: ~azure.mgmt.storagecache.models.CacheSku
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'health': {'readonly': True},
        'mount_addresses': {'readonly': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'CacheIdentity'},
        'cache_size_gb': {'key': 'properties.cacheSizeGB', 'type': 'int'},
        'health': {'key': 'properties.health', 'type': 'CacheHealth'},
        'mount_addresses': {'key': 'properties.mountAddresses', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'str'},
        'upgrade_status': {'key': 'properties.upgradeStatus', 'type': 'CacheUpgradeStatus'},
        'network_settings': {'key': 'properties.networkSettings', 'type': 'CacheNetworkSettings'},
        'encryption_settings': {'key': 'properties.encryptionSettings', 'type': 'CacheEncryptionSettings'},
        'security_settings': {'key': 'properties.securitySettings', 'type': 'CacheSecuritySettings'},
        'sku': {'key': 'sku', 'type': 'CacheSku'},
    }

    def __init__(self, *, tags=None, location: str=None, identity=None, cache_size_gb: int=None, provisioning_state=None, subnet: str=None, upgrade_status=None, network_settings=None, encryption_settings=None, security_settings=None, sku=None, **kwargs) -> None:
        super(Cache, self).__init__(**kwargs)
        self.tags = tags
        self.id = None
        self.location = location
        self.name = None
        self.type = None
        self.identity = identity
        self.cache_size_gb = cache_size_gb
        self.health = None
        self.mount_addresses = None
        self.provisioning_state = provisioning_state
        self.subnet = subnet
        self.upgrade_status = upgrade_status
        self.network_settings = network_settings
        self.encryption_settings = encryption_settings
        self.security_settings = security_settings
        self.sku = sku


class CacheEncryptionSettings(Model):
    """Cache encryption settings.

    :param key_encryption_key: Specifies the location of the key encryption
     key in Key Vault.
    :type key_encryption_key:
     ~azure.mgmt.storagecache.models.KeyVaultKeyReference
    """

    _attribute_map = {
        'key_encryption_key': {'key': 'keyEncryptionKey', 'type': 'KeyVaultKeyReference'},
    }

    def __init__(self, *, key_encryption_key=None, **kwargs) -> None:
        super(CacheEncryptionSettings, self).__init__(**kwargs)
        self.key_encryption_key = key_encryption_key


class CacheHealth(Model):
    """An indication of Cache health. Gives more information about health than
    just that related to provisioning.

    :param state: List of Cache health states. Possible values include:
     'Unknown', 'Healthy', 'Degraded', 'Down', 'Transitioning', 'Stopping',
     'Stopped', 'Upgrading', 'Flushing'
    :type state: str or ~azure.mgmt.storagecache.models.HealthStateType
    :param status_description: Describes explanation of state.
    :type status_description: str
    """

    _attribute_map = {
        'state': {'key': 'state', 'type': 'str'},
        'status_description': {'key': 'statusDescription', 'type': 'str'},
    }

    def __init__(self, *, state=None, status_description: str=None, **kwargs) -> None:
        super(CacheHealth, self).__init__(**kwargs)
        self.state = state
        self.status_description = status_description


class CacheIdentity(Model):
    """Cache identity properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal id of the cache.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id associated with the cache.
    :vartype tenant_id: str
    :param type: The type of identity used for the cache. Possible values
     include: 'SystemAssigned', 'None'
    :type type: str or ~azure.mgmt.storagecache.models.CacheIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'CacheIdentityType'},
    }

    def __init__(self, *, type=None, **kwargs) -> None:
        super(CacheIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class CacheNetworkSettings(Model):
    """Cache network settings.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param mtu: The IPv4 maximum transmission unit configured for the subnet.
     Default value: 1500 .
    :type mtu: int
    :ivar utility_addresses: Array of additional IP addresses used by this
     Cache.
    :vartype utility_addresses: list[str]
    """

    _validation = {
        'mtu': {'maximum': 1500, 'minimum': 576},
        'utility_addresses': {'readonly': True},
    }

    _attribute_map = {
        'mtu': {'key': 'mtu', 'type': 'int'},
        'utility_addresses': {'key': 'utilityAddresses', 'type': '[str]'},
    }

    def __init__(self, *, mtu: int=1500, **kwargs) -> None:
        super(CacheNetworkSettings, self).__init__(**kwargs)
        self.mtu = mtu
        self.utility_addresses = None


class CacheSecuritySettings(Model):
    """Cache security settings.

    :param root_squash: root squash of cache property.
    :type root_squash: bool
    """

    _attribute_map = {
        'root_squash': {'key': 'rootSquash', 'type': 'bool'},
    }

    def __init__(self, *, root_squash: bool=None, **kwargs) -> None:
        super(CacheSecuritySettings, self).__init__(**kwargs)
        self.root_squash = root_squash


class CacheSku(Model):
    """SKU for the Cache.

    :param name: SKU name for this Cache.
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, **kwargs) -> None:
        super(CacheSku, self).__init__(**kwargs)
        self.name = name


class CacheUpgradeStatus(Model):
    """Properties describing the software upgrade state of the Cache.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar current_firmware_version: Version string of the firmware currently
     installed on this Cache.
    :vartype current_firmware_version: str
    :ivar firmware_update_status: True if there is a firmware update ready to
     install on this Cache. The firmware will automatically be installed after
     firmwareUpdateDeadline if not triggered earlier via the upgrade operation.
     Possible values include: 'available', 'unavailable'
    :vartype firmware_update_status: str or
     ~azure.mgmt.storagecache.models.FirmwareStatusType
    :ivar firmware_update_deadline: Time at which the pending firmware update
     will automatically be installed on the Cache.
    :vartype firmware_update_deadline: datetime
    :ivar last_firmware_update: Time of the last successful firmware update.
    :vartype last_firmware_update: datetime
    :ivar pending_firmware_version: When firmwareUpdateAvailable is true, this
     field holds the version string for the update.
    :vartype pending_firmware_version: str
    """

    _validation = {
        'current_firmware_version': {'readonly': True},
        'firmware_update_status': {'readonly': True},
        'firmware_update_deadline': {'readonly': True},
        'last_firmware_update': {'readonly': True},
        'pending_firmware_version': {'readonly': True},
    }

    _attribute_map = {
        'current_firmware_version': {'key': 'currentFirmwareVersion', 'type': 'str'},
        'firmware_update_status': {'key': 'firmwareUpdateStatus', 'type': 'str'},
        'firmware_update_deadline': {'key': 'firmwareUpdateDeadline', 'type': 'iso-8601'},
        'last_firmware_update': {'key': 'lastFirmwareUpdate', 'type': 'iso-8601'},
        'pending_firmware_version': {'key': 'pendingFirmwareVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(CacheUpgradeStatus, self).__init__(**kwargs)
        self.current_firmware_version = None
        self.firmware_update_status = None
        self.firmware_update_deadline = None
        self.last_firmware_update = None
        self.pending_firmware_version = None


class ClfsTarget(Model):
    """Properties pertained to ClfsTarget.

    :param target: Resource ID of storage container.
    :type target: str
    """

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, *, target: str=None, **kwargs) -> None:
        super(ClfsTarget, self).__init__(**kwargs)
        self.target = target


class CloudError(Model):
    """An error response.

    :param error: The body of the error.
    :type error: ~azure.mgmt.storagecache.models.CloudErrorBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CloudErrorBody'},
    }

    def __init__(self, *, error=None, **kwargs) -> None:
        super(CloudError, self).__init__(**kwargs)
        self.error = error


class CloudErrorException(HttpOperationError):
    """Server responsed with exception of type: 'CloudError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(CloudErrorException, self).__init__(deserialize, response, 'CloudError', *args)


class CloudErrorBody(Model):
    """An error response.

    :param code: An identifier for the error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param details: A list of additional details about the error.
    :type details: list[~azure.mgmt.storagecache.models.CloudErrorBody]
    :param message: A message describing the error, intended to be suitable
     for display in a user interface.
    :type message: str
    :param target: The target of the particular error. For example, the name
     of the property in error.
    :type target: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, details=None, message: str=None, target: str=None, **kwargs) -> None:
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.details = details
        self.message = message
        self.target = target


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class KeyVaultKeyReference(Model):
    """Describes a reference to Key Vault Key.

    All required parameters must be populated in order to send to Azure.

    :param key_url: Required. The URL referencing a key encryption key in Key
     Vault.
    :type key_url: str
    :param source_vault: Required. Describes a resource Id to source Key
     Vault.
    :type source_vault:
     ~azure.mgmt.storagecache.models.KeyVaultKeyReferenceSourceVault
    """

    _validation = {
        'key_url': {'required': True},
        'source_vault': {'required': True},
    }

    _attribute_map = {
        'key_url': {'key': 'keyUrl', 'type': 'str'},
        'source_vault': {'key': 'sourceVault', 'type': 'KeyVaultKeyReferenceSourceVault'},
    }

    def __init__(self, *, key_url: str, source_vault, **kwargs) -> None:
        super(KeyVaultKeyReference, self).__init__(**kwargs)
        self.key_url = key_url
        self.source_vault = source_vault


class KeyVaultKeyReferenceSourceVault(Model):
    """Describes a resource Id to source Key Vault.

    :param id: Resource Id.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(KeyVaultKeyReferenceSourceVault, self).__init__(**kwargs)
        self.id = id


class NamespaceJunction(Model):
    """A namespace junction.

    :param namespace_path: Namespace path on a Cache for a Storage Target.
    :type namespace_path: str
    :param target_path: Path in Storage Target to which namespacePath points.
    :type target_path: str
    :param nfs_export: NFS export where targetPath exists.
    :type nfs_export: str
    """

    _attribute_map = {
        'namespace_path': {'key': 'namespacePath', 'type': 'str'},
        'target_path': {'key': 'targetPath', 'type': 'str'},
        'nfs_export': {'key': 'nfsExport', 'type': 'str'},
    }

    def __init__(self, *, namespace_path: str=None, target_path: str=None, nfs_export: str=None, **kwargs) -> None:
        super(NamespaceJunction, self).__init__(**kwargs)
        self.namespace_path = namespace_path
        self.target_path = target_path
        self.nfs_export = nfs_export


class Nfs3Target(Model):
    """Properties pertained to Nfs3Target.

    :param target: IP address or host name of an NFSv3 host (e.g.,
     10.0.44.44).
    :type target: str
    :param usage_model: Identifies the primary usage model to be used for this
     Storage Target. Get choices from .../usageModels
    :type usage_model: str
    """

    _validation = {
        'target': {'pattern': r'^[-.0-9a-zA-Z]+$'},
    }

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
        'usage_model': {'key': 'usageModel', 'type': 'str'},
    }

    def __init__(self, *, target: str=None, usage_model: str=None, **kwargs) -> None:
        super(Nfs3Target, self).__init__(**kwargs)
        self.target = target
        self.usage_model = usage_model


class ResourceSku(Model):
    """A resource SKU.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar resource_type: The type of resource the SKU applies to.
    :vartype resource_type: str
    :param capabilities: A list of capabilities of this SKU, such as
     throughput or ops/sec.
    :type capabilities:
     list[~azure.mgmt.storagecache.models.ResourceSkuCapabilities]
    :ivar locations: The set of locations that the SKU is available. This will
     be supported and registered Azure Geo Regions (e.g., West US, East US,
     Southeast Asia, etc.).
    :vartype locations: list[str]
    :param location_info: The set of locations that the SKU is available.
    :type location_info:
     list[~azure.mgmt.storagecache.models.ResourceSkuLocationInfo]
    :param name: The name of this SKU.
    :type name: str
    :param restrictions: The restrictions preventing this SKU from being used.
     This is empty if there are no restrictions.
    :type restrictions: list[~azure.mgmt.storagecache.models.Restriction]
    """

    _validation = {
        'resource_type': {'readonly': True},
        'locations': {'readonly': True},
    }

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'capabilities': {'key': 'capabilities', 'type': '[ResourceSkuCapabilities]'},
        'locations': {'key': 'locations', 'type': '[str]'},
        'location_info': {'key': 'locationInfo', 'type': '[ResourceSkuLocationInfo]'},
        'name': {'key': 'name', 'type': 'str'},
        'restrictions': {'key': 'restrictions', 'type': '[Restriction]'},
    }

    def __init__(self, *, capabilities=None, location_info=None, name: str=None, restrictions=None, **kwargs) -> None:
        super(ResourceSku, self).__init__(**kwargs)
        self.resource_type = None
        self.capabilities = capabilities
        self.locations = None
        self.location_info = location_info
        self.name = name
        self.restrictions = restrictions


class ResourceSkuCapabilities(Model):
    """A resource SKU capability.

    :param name: Name of a capability, such as ops/sec.
    :type name: str
    :param value: Quantity, if the capability is measured by quantity.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, value: str=None, **kwargs) -> None:
        super(ResourceSkuCapabilities, self).__init__(**kwargs)
        self.name = name
        self.value = value


class ResourceSkuLocationInfo(Model):
    """Resource SKU location information.

    :param location: Location where this SKU is available.
    :type location: str
    :param zones: Zones if any.
    :type zones: list[str]
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'zones': {'key': 'zones', 'type': '[str]'},
    }

    def __init__(self, *, location: str=None, zones=None, **kwargs) -> None:
        super(ResourceSkuLocationInfo, self).__init__(**kwargs)
        self.location = location
        self.zones = zones


class Restriction(Model):
    """The restrictions preventing this SKU from being used.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of restrictions. In this version, the only possible
     value for this is location.
    :vartype type: str
    :ivar values: The value of restrictions. If the restriction type is set to
     location, then this would be the different locations where the SKU is
     restricted.
    :vartype values: list[str]
    :param reason_code: The reason for the restriction. As of now this can be
     "QuotaId" or "NotAvailableForSubscription". "QuotaId" is set when the SKU
     has requiredQuotas parameter as the subscription does not belong to that
     quota. "NotAvailableForSubscription" is related to capacity at the
     datacenter. Possible values include: 'QuotaId',
     'NotAvailableForSubscription'
    :type reason_code: str or ~azure.mgmt.storagecache.models.ReasonCode
    """

    _validation = {
        'type': {'readonly': True},
        'values': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'},
        'reason_code': {'key': 'reasonCode', 'type': 'str'},
    }

    def __init__(self, *, reason_code=None, **kwargs) -> None:
        super(Restriction, self).__init__(**kwargs)
        self.type = None
        self.values = None
        self.reason_code = reason_code


class StorageTargetResource(Model):
    """Resource used by a Cache.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the Storage Target.
    :vartype name: str
    :ivar id: Resource ID of the Storage Target.
    :vartype id: str
    :ivar type: Type of the Storage Target;
     Microsoft.StorageCache/Cache/StorageTarget
    :vartype type: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(StorageTargetResource, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None


class StorageTarget(StorageTargetResource):
    """Type of the Storage Target.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Name of the Storage Target.
    :vartype name: str
    :ivar id: Resource ID of the Storage Target.
    :vartype id: str
    :ivar type: Type of the Storage Target;
     Microsoft.StorageCache/Cache/StorageTarget
    :vartype type: str
    :param junctions: List of Cache namespace junctions to target for
     namespace associations.
    :type junctions: list[~azure.mgmt.storagecache.models.NamespaceJunction]
    :param target_type: Required. Type of the Storage Target. Possible values
     include: 'nfs3', 'clfs', 'unknown'
    :type target_type: str or
     ~azure.mgmt.storagecache.models.StorageTargetType
    :param provisioning_state: ARM provisioning state, see
     https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property.
     Possible values include: 'Succeeded', 'Failed', 'Cancelled', 'Creating',
     'Deleting', 'Updating'
    :type provisioning_state: str or
     ~azure.mgmt.storagecache.models.ProvisioningStateType
    :param nfs3: Properties when targetType is nfs3.
    :type nfs3: ~azure.mgmt.storagecache.models.Nfs3Target
    :param clfs: Properties when targetType is clfs.
    :type clfs: ~azure.mgmt.storagecache.models.ClfsTarget
    :param unknown: Properties when targetType is unknown.
    :type unknown: ~azure.mgmt.storagecache.models.UnknownTarget
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'target_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'junctions': {'key': 'properties.junctions', 'type': '[NamespaceJunction]'},
        'target_type': {'key': 'properties.targetType', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'nfs3': {'key': 'properties.nfs3', 'type': 'Nfs3Target'},
        'clfs': {'key': 'properties.clfs', 'type': 'ClfsTarget'},
        'unknown': {'key': 'properties.unknown', 'type': 'UnknownTarget'},
    }

    def __init__(self, *, target_type, junctions=None, provisioning_state=None, nfs3=None, clfs=None, unknown=None, **kwargs) -> None:
        super(StorageTarget, self).__init__(**kwargs)
        self.junctions = junctions
        self.target_type = target_type
        self.provisioning_state = provisioning_state
        self.nfs3 = nfs3
        self.clfs = clfs
        self.unknown = unknown


class UnknownTarget(Model):
    """Properties pertained to UnknownTarget.

    :param unknown_map: Dictionary of string->string pairs containing
     information about the Storage Target.
    :type unknown_map: dict[str, str]
    """

    _attribute_map = {
        'unknown_map': {'key': 'unknownMap', 'type': '{str}'},
    }

    def __init__(self, *, unknown_map=None, **kwargs) -> None:
        super(UnknownTarget, self).__init__(**kwargs)
        self.unknown_map = unknown_map


class UsageModel(Model):
    """A usage model.

    :param display: Localized information describing this usage model.
    :type display: ~azure.mgmt.storagecache.models.UsageModelDisplay
    :param model_name: Non-localized keyword name for this usage model.
    :type model_name: str
    :param target_type: The type of Storage Target to which this model is
     applicable (only nfs3 as of this version).
    :type target_type: str
    """

    _attribute_map = {
        'display': {'key': 'display', 'type': 'UsageModelDisplay'},
        'model_name': {'key': 'modelName', 'type': 'str'},
        'target_type': {'key': 'targetType', 'type': 'str'},
    }

    def __init__(self, *, display=None, model_name: str=None, target_type: str=None, **kwargs) -> None:
        super(UsageModel, self).__init__(**kwargs)
        self.display = display
        self.model_name = model_name
        self.target_type = target_type


class UsageModelDisplay(Model):
    """Localized information describing this usage model.

    :param description: String to display for this usage model.
    :type description: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, **kwargs) -> None:
        super(UsageModelDisplay, self).__init__(**kwargs)
        self.description = description
