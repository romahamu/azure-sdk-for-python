# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ServiceOperations:
    """ServiceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.databox.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_available_skus(
        self,
        location: str,
        available_sku_request: "_models.AvailableSkuRequest",
        **kwargs
    ) -> AsyncIterable["_models.AvailableSkusResult"]:
        """This method provides the list of available skus for the given subscription and location.

        :param location: The location of the resource.
        :type location: str
        :param available_sku_request: Filters for showing the available skus.
        :type available_sku_request: ~azure.mgmt.databox.models.AvailableSkuRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AvailableSkusResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.databox.models.AvailableSkusResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AvailableSkusResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-01-01"
        content_type = "application/json"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_available_skus.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'location': self._serialize.url("location", location, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                body_content_kwargs = {}  # type: Dict[str, Any]
                body_content = self._serialize.body(available_sku_request, 'AvailableSkuRequest')
                body_content_kwargs['content'] = body_content
                request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                body_content_kwargs = {}  # type: Dict[str, Any]
                body_content = self._serialize.body(available_sku_request, 'AvailableSkuRequest')
                body_content_kwargs['content'] = body_content
                request = self._client.get(url, query_parameters, header_parameters, **body_content_kwargs)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('AvailableSkusResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_available_skus.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/availableSkus'}  # type: ignore

    async def validate_address(
        self,
        location: str,
        validate_address: "_models.ValidateAddress",
        **kwargs
    ) -> "_models.AddressValidationOutput":
        """This method validates the customer shipping address and provide alternate addresses if any.

        :param location: The location of the resource.
        :type location: str
        :param validate_address: Shipping address of the customer.
        :type validate_address: ~azure.mgmt.databox.models.ValidateAddress
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddressValidationOutput, or the result of cls(response)
        :rtype: ~azure.mgmt.databox.models.AddressValidationOutput
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AddressValidationOutput"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-01-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.validate_address.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(validate_address, 'ValidateAddress')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AddressValidationOutput', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    validate_address.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataBox/locations/{location}/validateAddress'}  # type: ignore
