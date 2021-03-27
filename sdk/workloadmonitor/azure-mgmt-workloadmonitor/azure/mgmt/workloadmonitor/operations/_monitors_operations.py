# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MonitorsOperations(object):
    """MonitorsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~workload_monitor_api.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        resource_namespace,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        filter=None,  # type: Optional[str]
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.MonitorList"]
        """Get list of a monitors of a resource (with optional filter).

        Get list of a monitors of a resource (with optional filter).

        :param subscription_id: The subscriptionId of the resource.
        :type subscription_id: str
        :param resource_group_name: The resourceGroupName of the resource.
        :type resource_group_name: str
        :param resource_namespace: The resourceNamespace of the resource.
        :type resource_namespace: str
        :param resource_type: The resourceType of the resource.
        :type resource_type: str
        :param resource_name: The resourceType of the resource.
        :type resource_name: str
        :param filter: list example: $filter=monitorName eq 'logical-disks|C:|disk-free-space-mb';
         history example: $filter=isHeartbeat eq false.
        :type filter: str
        :param expand: ex: $expand=evidence,configuration.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MonitorList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~workload_monitor_api.models.MonitorList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MonitorList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-13-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'resourceNamespace': self._serialize.url("resource_namespace", resource_namespace, 'str'),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MonitorList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DefaultError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.WorkloadMonitor/monitors'}  # type: ignore

    def get(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        resource_namespace,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        monitor_id,  # type: str
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Monitor"
        """Get the current status of a monitor of a resource.

        Get the current status of a monitor of a resource.

        :param subscription_id: The subscriptionId of the resource.
        :type subscription_id: str
        :param resource_group_name: The resourceGroupName of the resource.
        :type resource_group_name: str
        :param resource_namespace: The resourceNamespace of the resource.
        :type resource_namespace: str
        :param resource_type: The resourceType of the resource.
        :type resource_type: str
        :param resource_name: The resourceType of the resource.
        :type resource_name: str
        :param monitor_id: The monitorId of the resource (url encoded).
        :type monitor_id: str
        :param expand: ex: $expand=evidence,configuration.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Monitor, or the result of cls(response)
        :rtype: ~workload_monitor_api.models.Monitor
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Monitor"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-13-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceNamespace': self._serialize.url("resource_namespace", resource_namespace, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'monitorId': self._serialize.url("monitor_id", monitor_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DefaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Monitor', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.WorkloadMonitor/monitors/{monitorId}'}  # type: ignore

    def list_state_changes(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        resource_namespace,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        monitor_id,  # type: str
        filter=None,  # type: Optional[str]
        expand=None,  # type: Optional[str]
        start_timestamp_utc=None,  # type: Optional[datetime.datetime]
        end_timestamp_utc=None,  # type: Optional[datetime.datetime]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.MonitorStateChangeList"]
        """Get history of a monitor of a resource (with optional filter).

        Get history of a monitor of a resource (with optional filter).

        :param subscription_id: The subscriptionId of the resource.
        :type subscription_id: str
        :param resource_group_name: The resourceGroupName of the resource.
        :type resource_group_name: str
        :param resource_namespace: The resourceNamespace of the resource.
        :type resource_namespace: str
        :param resource_type: The resourceType of the resource.
        :type resource_type: str
        :param resource_name: The resourceType of the resource.
        :type resource_name: str
        :param monitor_id: The monitorId of the resource (url encoded).
        :type monitor_id: str
        :param filter: list example: $filter=monitorName eq 'logical-disks|C:|disk-free-space-mb';
         history example: $filter=isHeartbeat eq false.
        :type filter: str
        :param expand: ex: $expand=evidence,configuration.
        :type expand: str
        :param start_timestamp_utc: The start Timestamp for the desired history.
        :type start_timestamp_utc: ~datetime.datetime
        :param end_timestamp_utc: The end Timestamp for the desired history.
        :type end_timestamp_utc: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MonitorStateChangeList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~workload_monitor_api.models.MonitorStateChangeList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MonitorStateChangeList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-13-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_state_changes.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'resourceNamespace': self._serialize.url("resource_namespace", resource_namespace, 'str'),
                    'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
                    'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
                    'monitorId': self._serialize.url("monitor_id", monitor_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                if start_timestamp_utc is not None:
                    query_parameters['startTimestampUtc'] = self._serialize.query("start_timestamp_utc", start_timestamp_utc, 'iso-8601')
                if end_timestamp_utc is not None:
                    query_parameters['endTimestampUtc'] = self._serialize.query("end_timestamp_utc", end_timestamp_utc, 'iso-8601')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MonitorStateChangeList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DefaultError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_state_changes.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.WorkloadMonitor/monitors/{monitorId}/history'}  # type: ignore

    def get_state_change(
        self,
        subscription_id,  # type: str
        resource_group_name,  # type: str
        resource_namespace,  # type: str
        resource_type,  # type: str
        resource_name,  # type: str
        monitor_id,  # type: str
        timestamp_unix,  # type: str
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MonitorStateChange"
        """Get the status of a monitor at a specific timestamp in history.

        Get the status of a monitor at a specific timestamp in history.

        :param subscription_id: The subscriptionId of the resource.
        :type subscription_id: str
        :param resource_group_name: The resourceGroupName of the resource.
        :type resource_group_name: str
        :param resource_namespace: The resourceNamespace of the resource.
        :type resource_namespace: str
        :param resource_type: The resourceType of the resource.
        :type resource_type: str
        :param resource_name: The resourceType of the resource.
        :type resource_name: str
        :param monitor_id: The monitorId of the resource (url encoded).
        :type monitor_id: str
        :param timestamp_unix: The timestamp of the state change (Unix format).
        :type timestamp_unix: str
        :param expand: ex: $expand=evidence,configuration.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MonitorStateChange, or the result of cls(response)
        :rtype: ~workload_monitor_api.models.MonitorStateChange
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MonitorStateChange"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-13-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_state_change.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'resourceNamespace': self._serialize.url("resource_namespace", resource_namespace, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
            'resourceName': self._serialize.url("resource_name", resource_name, 'str'),
            'monitorId': self._serialize.url("monitor_id", monitor_id, 'str'),
            'timestampUnix': self._serialize.url("timestamp_unix", timestamp_unix, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DefaultError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MonitorStateChange', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_state_change.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceNamespace}/{resourceType}/{resourceName}/providers/Microsoft.WorkloadMonitor/monitors/{monitorId}/history/{timestampUnix}'}  # type: ignore
