# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import ManagedLabsClientConfiguration
from .operations import ProviderOperationsOperations
from .operations import GlobalUsersOperations
from .operations import LabAccountsOperations
from .operations import Operations
from .operations import GalleryImagesOperations
from .operations import LabsOperations
from .operations import EnvironmentSettingsOperations
from .operations import EnvironmentsOperations
from .operations import UsersOperations
from . import models


class ManagedLabsClient(object):
    """The Managed Labs Client.

    :ivar provider_operations: ProviderOperationsOperations operations
    :vartype provider_operations: azure.mgmt.labservices.operations.ProviderOperationsOperations
    :ivar global_users: GlobalUsersOperations operations
    :vartype global_users: azure.mgmt.labservices.operations.GlobalUsersOperations
    :ivar lab_accounts: LabAccountsOperations operations
    :vartype lab_accounts: azure.mgmt.labservices.operations.LabAccountsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.labservices.operations.Operations
    :ivar gallery_images: GalleryImagesOperations operations
    :vartype gallery_images: azure.mgmt.labservices.operations.GalleryImagesOperations
    :ivar labs: LabsOperations operations
    :vartype labs: azure.mgmt.labservices.operations.LabsOperations
    :ivar environment_settings: EnvironmentSettingsOperations operations
    :vartype environment_settings: azure.mgmt.labservices.operations.EnvironmentSettingsOperations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: azure.mgmt.labservices.operations.EnvironmentsOperations
    :ivar users: UsersOperations operations
    :vartype users: azure.mgmt.labservices.operations.UsersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ManagedLabsClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.provider_operations = ProviderOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.global_users = GlobalUsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.lab_accounts = LabAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.gallery_images = GalleryImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.labs = LabsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_settings = EnvironmentSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ManagedLabsClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
