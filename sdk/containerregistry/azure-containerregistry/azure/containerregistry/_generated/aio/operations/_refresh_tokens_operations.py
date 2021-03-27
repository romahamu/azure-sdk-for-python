# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class RefreshTokensOperations:
    """RefreshTokensOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.containerregistry.models
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

    async def get_from_exchange(
        self,
        grant_type: Union[str, "_models.PostContentSchemaGrantType"],
        service: str,
        tenant: Optional[str] = None,
        refresh_token: Optional[str] = None,
        access_token: Optional[str] = None,
        **kwargs
    ) -> "_models.RefreshToken":
        """Exchange AAD tokens for an ACR refresh Token.

        :param grant_type: Can take a value of access_token_refresh_token, or access_token, or
         refresh_token.
        :type grant_type: str or ~azure.containerregistry.models.PostContentSchemaGrantType
        :param service: Indicates the name of your Azure container registry.
        :type service: str
        :param tenant: AAD tenant associated to the AAD credentials.
        :type tenant: str
        :param refresh_token: AAD refresh token, mandatory when grant_type is
         access_token_refresh_token or refresh_token.
        :type refresh_token: str
        :param access_token: AAD access token, mandatory when grant_type is access_token_refresh_token
         or access_token.
        :type access_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RefreshToken, or the result of cls(response)
        :rtype: ~azure.containerregistry.models.RefreshToken
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.RefreshToken"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")
        accept = "application/json"

        # Construct URL
        url = self.get_from_exchange.metadata['url']  # type: ignore
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(grant_type, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AcrErrors, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('RefreshToken', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_from_exchange.metadata = {'url': '/oauth2/exchange'}  # type: ignore
