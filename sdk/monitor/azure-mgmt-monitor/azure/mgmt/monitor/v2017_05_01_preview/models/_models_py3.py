# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._monitor_management_client_enums import *


class ProxyOnlyResource(msrest.serialization.Model):
    """A proxy only azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyOnlyResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class DiagnosticSettingsCategoryResource(ProxyOnlyResource):
    """The diagnostic settings category resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param category_type: The type of the diagnostic settings category. Possible values include:
     "Metrics", "Logs".
    :type category_type: str or ~$(python-base-namespace).v2017_05_01_preview.models.CategoryType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'category_type': {'key': 'properties.categoryType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        category_type: Optional[Union[str, "CategoryType"]] = None,
        **kwargs
    ):
        super(DiagnosticSettingsCategoryResource, self).__init__(**kwargs)
        self.category_type = category_type


class DiagnosticSettingsCategoryResourceCollection(msrest.serialization.Model):
    """Represents a collection of diagnostic setting category resources.

    :param value: The collection of diagnostic settings category resources.
    :type value: list[~$(python-base-
     namespace).v2017_05_01_preview.models.DiagnosticSettingsCategoryResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DiagnosticSettingsCategoryResource]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DiagnosticSettingsCategoryResource"]] = None,
        **kwargs
    ):
        super(DiagnosticSettingsCategoryResourceCollection, self).__init__(**kwargs)
        self.value = value


class DiagnosticSettingsResource(ProxyOnlyResource):
    """The diagnostic setting resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param storage_account_id: The resource ID of the storage account to which you would like to
     send Diagnostic Logs.
    :type storage_account_id: str
    :param service_bus_rule_id: The service bus rule Id of the diagnostic setting. This is here to
     maintain backwards compatibility.
    :type service_bus_rule_id: str
    :param event_hub_authorization_rule_id: The resource Id for the event hub authorization rule.
    :type event_hub_authorization_rule_id: str
    :param event_hub_name: The name of the event hub. If none is specified, the default event hub
     will be selected.
    :type event_hub_name: str
    :param metrics: The list of metric settings.
    :type metrics: list[~$(python-base-namespace).v2017_05_01_preview.models.MetricSettings]
    :param logs: The list of logs settings.
    :type logs: list[~$(python-base-namespace).v2017_05_01_preview.models.LogSettings]
    :param workspace_id: The full ARM resource ID of the Log Analytics workspace to which you would
     like to send Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-
     integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
    :type workspace_id: str
    :param log_analytics_destination_type: A string indicating whether the export to Log Analytics
     should use the default destination type, i.e. AzureDiagnostics, or use a destination type
     constructed as follows: :code:`<normalized service identity>`_:code:`<normalized category
     name>`. Possible values are: Dedicated and null (null is default.).
    :type log_analytics_destination_type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'event_hub_authorization_rule_id': {'key': 'properties.eventHubAuthorizationRuleId', 'type': 'str'},
        'event_hub_name': {'key': 'properties.eventHubName', 'type': 'str'},
        'metrics': {'key': 'properties.metrics', 'type': '[MetricSettings]'},
        'logs': {'key': 'properties.logs', 'type': '[LogSettings]'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
        'log_analytics_destination_type': {'key': 'properties.logAnalyticsDestinationType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        storage_account_id: Optional[str] = None,
        service_bus_rule_id: Optional[str] = None,
        event_hub_authorization_rule_id: Optional[str] = None,
        event_hub_name: Optional[str] = None,
        metrics: Optional[List["MetricSettings"]] = None,
        logs: Optional[List["LogSettings"]] = None,
        workspace_id: Optional[str] = None,
        log_analytics_destination_type: Optional[str] = None,
        **kwargs
    ):
        super(DiagnosticSettingsResource, self).__init__(**kwargs)
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.event_hub_name = event_hub_name
        self.metrics = metrics
        self.logs = logs
        self.workspace_id = workspace_id
        self.log_analytics_destination_type = log_analytics_destination_type


class DiagnosticSettingsResourceCollection(msrest.serialization.Model):
    """Represents a collection of alert rule resources.

    :param value: The collection of diagnostic settings resources;.
    :type value: list[~$(python-base-
     namespace).v2017_05_01_preview.models.DiagnosticSettingsResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DiagnosticSettingsResource]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DiagnosticSettingsResource"]] = None,
        **kwargs
    ):
        super(DiagnosticSettingsResourceCollection, self).__init__(**kwargs)
        self.value = value


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class LocalizableString(msrest.serialization.Model):
    """The localizable string class.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. the invariant value.
    :type value: str
    :param localized_value: the locale specific value.
    :type localized_value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: str,
        localized_value: Optional[str] = None,
        **kwargs
    ):
        super(LocalizableString, self).__init__(**kwargs)
        self.value = value
        self.localized_value = localized_value


class LogSettings(msrest.serialization.Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular log.

    All required parameters must be populated in order to send to Azure.

    :param category: Name of a Diagnostic Log category for a resource type this setting is applied
     to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET
     diagnostic settings operation.
    :type category: str
    :param enabled: Required. a value indicating whether this log is enabled.
    :type enabled: bool
    :param retention_policy: the retention policy for this log.
    :type retention_policy: ~$(python-base-namespace).v2017_05_01_preview.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        category: Optional[str] = None,
        retention_policy: Optional["RetentionPolicy"] = None,
        **kwargs
    ):
        super(LogSettings, self).__init__(**kwargs)
        self.category = category
        self.enabled = enabled
        self.retention_policy = retention_policy


class MetadataValue(msrest.serialization.Model):
    """Represents a metric metadata value.

    :param name: the name of the metadata.
    :type name: ~$(python-base-namespace).v2017_05_01_preview.models.LocalizableString
    :param value: the value of the metadata.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional["LocalizableString"] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(MetadataValue, self).__init__(**kwargs)
        self.name = name
        self.value = value


class Metric(msrest.serialization.Model):
    """The result data of a query.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. the metric Id.
    :type id: str
    :param type: Required. the resource type of the metric resource.
    :type type: str
    :param name: Required. the name and the display name of the metric, i.e. it is localizable
     string.
    :type name: ~$(python-base-namespace).v2017_05_01_preview.models.LocalizableString
    :param unit: Required. the unit of the metric. Possible values include: "Count", "Bytes",
     "Seconds", "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds", "ByteSeconds",
     "Unspecified".
    :type unit: str or ~$(python-base-namespace).v2017_05_01_preview.models.Unit
    :param timeseries: Required. the time series returned when a data query is performed.
    :type timeseries: list[~$(python-base-namespace).v2017_05_01_preview.models.TimeSeriesElement]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'name': {'required': True},
        'unit': {'required': True},
        'timeseries': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'unit': {'key': 'unit', 'type': 'str'},
        'timeseries': {'key': 'timeseries', 'type': '[TimeSeriesElement]'},
    }

    def __init__(
        self,
        *,
        id: str,
        type: str,
        name: "LocalizableString",
        unit: Union[str, "Unit"],
        timeseries: List["TimeSeriesElement"],
        **kwargs
    ):
        super(Metric, self).__init__(**kwargs)
        self.id = id
        self.type = type
        self.name = name
        self.unit = unit
        self.timeseries = timeseries


class MetricAvailability(msrest.serialization.Model):
    """Metric availability specifies the time grain (aggregation interval or frequency) and the retention period for that time grain.

    :param time_grain: the time grain specifies the aggregation interval for the metric. Expressed
     as a duration 'PT1M', 'P1D', etc.
    :type time_grain: ~datetime.timedelta
    :param retention: the retention period for the metric at the specified timegrain.  Expressed as
     a duration 'PT1M', 'P1D', etc.
    :type retention: ~datetime.timedelta
    """

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'duration'},
        'retention': {'key': 'retention', 'type': 'duration'},
    }

    def __init__(
        self,
        *,
        time_grain: Optional[datetime.timedelta] = None,
        retention: Optional[datetime.timedelta] = None,
        **kwargs
    ):
        super(MetricAvailability, self).__init__(**kwargs)
        self.time_grain = time_grain
        self.retention = retention


class MetricDefinition(msrest.serialization.Model):
    """Metric definition class specifies the metadata for a metric.

    :param is_dimension_required: Flag to indicate whether the dimension is required.
    :type is_dimension_required: bool
    :param resource_id: the resource identifier of the resource that emitted the metric.
    :type resource_id: str
    :param name: the name and the display name of the metric, i.e. it is a localizable string.
    :type name: ~$(python-base-namespace).v2017_05_01_preview.models.LocalizableString
    :param unit: the unit of the metric. Possible values include: "Count", "Bytes", "Seconds",
     "CountPerSecond", "BytesPerSecond", "Percent", "MilliSeconds", "ByteSeconds", "Unspecified".
    :type unit: str or ~$(python-base-namespace).v2017_05_01_preview.models.Unit
    :param primary_aggregation_type: the primary aggregation type value defining how to use the
     values for display. Possible values include: "None", "Average", "Count", "Minimum", "Maximum",
     "Total".
    :type primary_aggregation_type: str or ~$(python-base-
     namespace).v2017_05_01_preview.models.AggregationType
    :param metric_availabilities: the collection of what aggregation intervals are available to be
     queried.
    :type metric_availabilities: list[~$(python-base-
     namespace).v2017_05_01_preview.models.MetricAvailability]
    :param id: the resource identifier of the metric definition.
    :type id: str
    :param dimensions: the name and the display name of the dimension, i.e. it is a localizable
     string.
    :type dimensions: list[~$(python-base-namespace).v2017_05_01_preview.models.LocalizableString]
    """

    _attribute_map = {
        'is_dimension_required': {'key': 'isDimensionRequired', 'type': 'bool'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'unit': {'key': 'unit', 'type': 'str'},
        'primary_aggregation_type': {'key': 'primaryAggregationType', 'type': 'str'},
        'metric_availabilities': {'key': 'metricAvailabilities', 'type': '[MetricAvailability]'},
        'id': {'key': 'id', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[LocalizableString]'},
    }

    def __init__(
        self,
        *,
        is_dimension_required: Optional[bool] = None,
        resource_id: Optional[str] = None,
        name: Optional["LocalizableString"] = None,
        unit: Optional[Union[str, "Unit"]] = None,
        primary_aggregation_type: Optional[Union[str, "AggregationType"]] = None,
        metric_availabilities: Optional[List["MetricAvailability"]] = None,
        id: Optional[str] = None,
        dimensions: Optional[List["LocalizableString"]] = None,
        **kwargs
    ):
        super(MetricDefinition, self).__init__(**kwargs)
        self.is_dimension_required = is_dimension_required
        self.resource_id = resource_id
        self.name = name
        self.unit = unit
        self.primary_aggregation_type = primary_aggregation_type
        self.metric_availabilities = metric_availabilities
        self.id = id
        self.dimensions = dimensions


class MetricDefinitionCollection(msrest.serialization.Model):
    """Represents collection of metric definitions.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. the values for the metric definitions.
    :type value: list[~$(python-base-namespace).v2017_05_01_preview.models.MetricDefinition]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MetricDefinition]'},
    }

    def __init__(
        self,
        *,
        value: List["MetricDefinition"],
        **kwargs
    ):
        super(MetricDefinitionCollection, self).__init__(**kwargs)
        self.value = value


class MetricSettings(msrest.serialization.Model):
    """Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular metric.

    All required parameters must be populated in order to send to Azure.

    :param time_grain: the timegrain of the metric in ISO8601 format.
    :type time_grain: ~datetime.timedelta
    :param category: Name of a Diagnostic Metric category for a resource type this setting is
     applied to. To obtain the list of Diagnostic metric categories for a resource, first perform a
     GET diagnostic settings operation.
    :type category: str
    :param enabled: Required. a value indicating whether this category is enabled.
    :type enabled: bool
    :param retention_policy: the retention policy for this category.
    :type retention_policy: ~$(python-base-namespace).v2017_05_01_preview.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'duration'},
        'category': {'key': 'category', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        time_grain: Optional[datetime.timedelta] = None,
        category: Optional[str] = None,
        retention_policy: Optional["RetentionPolicy"] = None,
        **kwargs
    ):
        super(MetricSettings, self).__init__(**kwargs)
        self.time_grain = time_grain
        self.category = category
        self.enabled = enabled
        self.retention_policy = retention_policy


class MetricValue(msrest.serialization.Model):
    """Represents a metric value.

    All required parameters must be populated in order to send to Azure.

    :param time_stamp: Required. the timestamp for the metric value in ISO 8601 format.
    :type time_stamp: ~datetime.datetime
    :param average: the average value in the time range.
    :type average: float
    :param minimum: the least value in the time range.
    :type minimum: float
    :param maximum: the greatest value in the time range.
    :type maximum: float
    :param total: the sum of all of the values in the time range.
    :type total: float
    :param count: the number of samples in the time range. Can be used to determine the number of
     values that contributed to the average value.
    :type count: long
    """

    _validation = {
        'time_stamp': {'required': True},
    }

    _attribute_map = {
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'average': {'key': 'average', 'type': 'float'},
        'minimum': {'key': 'minimum', 'type': 'float'},
        'maximum': {'key': 'maximum', 'type': 'float'},
        'total': {'key': 'total', 'type': 'float'},
        'count': {'key': 'count', 'type': 'long'},
    }

    def __init__(
        self,
        *,
        time_stamp: datetime.datetime,
        average: Optional[float] = None,
        minimum: Optional[float] = None,
        maximum: Optional[float] = None,
        total: Optional[float] = None,
        count: Optional[int] = None,
        **kwargs
    ):
        super(MetricValue, self).__init__(**kwargs)
        self.time_stamp = time_stamp
        self.average = average
        self.minimum = minimum
        self.maximum = maximum
        self.total = total
        self.count = count


class Response(msrest.serialization.Model):
    """The response to a metrics query.

    All required parameters must be populated in order to send to Azure.

    :param cost: The integer value representing the cost of the query, for data case.
    :type cost: int
    :param timespan: Required. The timespan for which the data was retrieved. Its value consists of
     two datetimes concatenated, separated by '/'.  This may be adjusted in the future and returned
     back from what was originally requested.
    :type timespan: str
    :param interval: The interval (window size) for which the metric data was returned in.  This
     may be adjusted in the future and returned back from what was originally requested.  This is
     not present if a metadata request was made.
    :type interval: ~datetime.timedelta
    :param value: Required. the value of the collection.
    :type value: list[~$(python-base-namespace).v2017_05_01_preview.models.Metric]
    """

    _validation = {
        'cost': {'minimum': 0},
        'timespan': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'cost': {'key': 'cost', 'type': 'int'},
        'timespan': {'key': 'timespan', 'type': 'str'},
        'interval': {'key': 'interval', 'type': 'duration'},
        'value': {'key': 'value', 'type': '[Metric]'},
    }

    def __init__(
        self,
        *,
        timespan: str,
        value: List["Metric"],
        cost: Optional[int] = None,
        interval: Optional[datetime.timedelta] = None,
        **kwargs
    ):
        super(Response, self).__init__(**kwargs)
        self.cost = cost
        self.timespan = timespan
        self.interval = interval
        self.value = value


class RetentionPolicy(msrest.serialization.Model):
    """Specifies the retention policy for the log.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. a value indicating whether the retention policy is enabled.
    :type enabled: bool
    :param days: Required. the number of days for the retention in days. A value of 0 will retain
     the events indefinitely.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'required': True, 'minimum': 0},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'days': {'key': 'days', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        days: int,
        **kwargs
    ):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = enabled
        self.days = days


class SubscriptionProxyOnlyResource(msrest.serialization.Model):
    """A proxy only azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        **kwargs
    ):
        super(SubscriptionProxyOnlyResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location


class SubscriptionDiagnosticSettingsResource(SubscriptionProxyOnlyResource):
    """The subscription diagnostic setting resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Location of the resource.
    :type location: str
    :param storage_account_id: The resource ID of the storage account to which you would like to
     send Diagnostic Logs.
    :type storage_account_id: str
    :param service_bus_rule_id: The service bus rule Id of the diagnostic setting. This is here to
     maintain backwards compatibility.
    :type service_bus_rule_id: str
    :param event_hub_authorization_rule_id: The resource Id for the event hub authorization rule.
    :type event_hub_authorization_rule_id: str
    :param event_hub_name: The name of the event hub. If none is specified, the default event hub
     will be selected.
    :type event_hub_name: str
    :param logs: The list of logs settings.
    :type logs: list[~$(python-base-namespace).v2017_05_01_preview.models.SubscriptionLogSettings]
    :param workspace_id: The full ARM resource ID of the Log Analytics workspace to which you would
     like to send Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-
     integration/providers/Microsoft.OperationalInsights/workspaces/viruela2.
    :type workspace_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'event_hub_authorization_rule_id': {'key': 'properties.eventHubAuthorizationRuleId', 'type': 'str'},
        'event_hub_name': {'key': 'properties.eventHubName', 'type': 'str'},
        'logs': {'key': 'properties.logs', 'type': '[SubscriptionLogSettings]'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        storage_account_id: Optional[str] = None,
        service_bus_rule_id: Optional[str] = None,
        event_hub_authorization_rule_id: Optional[str] = None,
        event_hub_name: Optional[str] = None,
        logs: Optional[List["SubscriptionLogSettings"]] = None,
        workspace_id: Optional[str] = None,
        **kwargs
    ):
        super(SubscriptionDiagnosticSettingsResource, self).__init__(location=location, **kwargs)
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.event_hub_name = event_hub_name
        self.logs = logs
        self.workspace_id = workspace_id


class SubscriptionDiagnosticSettingsResourceCollection(msrest.serialization.Model):
    """Represents a collection of subscription diagnostic settings resources.

    :param value: The collection of subscription diagnostic settings resources.
    :type value: list[~$(python-base-
     namespace).v2017_05_01_preview.models.SubscriptionDiagnosticSettingsResource]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SubscriptionDiagnosticSettingsResource]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["SubscriptionDiagnosticSettingsResource"]] = None,
        **kwargs
    ):
        super(SubscriptionDiagnosticSettingsResourceCollection, self).__init__(**kwargs)
        self.value = value


class SubscriptionLogSettings(msrest.serialization.Model):
    """Part of Subscription diagnostic setting. Specifies the settings for a particular log.

    All required parameters must be populated in order to send to Azure.

    :param category: Name of a Subscription Diagnostic Log category for a resource type this
     setting is applied to.
    :type category: str
    :param enabled: Required. a value indicating whether this log is enabled.
    :type enabled: bool
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        enabled: bool,
        category: Optional[str] = None,
        **kwargs
    ):
        super(SubscriptionLogSettings, self).__init__(**kwargs)
        self.category = category
        self.enabled = enabled


class TimeSeriesElement(msrest.serialization.Model):
    """A time series result type. The discriminator value is always TimeSeries in this case.

    :param metadatavalues: the metadata values returned if $filter was specified in the call.
    :type metadatavalues: list[~$(python-base-namespace).v2017_05_01_preview.models.MetadataValue]
    :param data: An array of data points representing the metric values.  This is only returned if
     a result type of data is specified.
    :type data: list[~$(python-base-namespace).v2017_05_01_preview.models.MetricValue]
    """

    _attribute_map = {
        'metadatavalues': {'key': 'metadatavalues', 'type': '[MetadataValue]'},
        'data': {'key': 'data', 'type': '[MetricValue]'},
    }

    def __init__(
        self,
        *,
        metadatavalues: Optional[List["MetadataValue"]] = None,
        data: Optional[List["MetricValue"]] = None,
        **kwargs
    ):
        super(TimeSeriesElement, self).__init__(**kwargs)
        self.metadatavalues = metadatavalues
        self.data = data
