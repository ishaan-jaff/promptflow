# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.0, generator: @autorest/python@5.12.2)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._flow_runs_admin_operations import build_check_policy_validation_async_request, build_get_storage_info_request, build_log_result_for_bulk_run_request, build_send_policy_validation_async_request, build_submit_bulk_run_async_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FlowRunsAdminOperations:
    """FlowRunsAdminOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~flow.models
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

    @distributed_trace_async
    async def submit_bulk_run_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        flow_id: str,
        bulk_run_id: str,
        **kwargs: Any
    ) -> "_models.FlowRunResult":
        """submit_bulk_run_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param flow_id:
        :type flow_id: str
        :param bulk_run_id:
        :type bulk_run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FlowRunResult, or the result of cls(response)
        :rtype: ~flow.models.FlowRunResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FlowRunResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_submit_bulk_run_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            flow_id=flow_id,
            bulk_run_id=bulk_run_id,
            template_url=self.submit_bulk_run_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('FlowRunResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    submit_bulk_run_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/FlowRunsAdmin/{flowId}/bulkRuns/{bulkRunId}/submit'}  # type: ignore


    @distributed_trace_async
    async def send_policy_validation_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        flow_id: str,
        bulk_run_id: str,
        **kwargs: Any
    ) -> "_models.PolicyValidationResponse":
        """send_policy_validation_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param flow_id:
        :type flow_id: str
        :param bulk_run_id:
        :type bulk_run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyValidationResponse, or the result of cls(response)
        :rtype: ~flow.models.PolicyValidationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyValidationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_send_policy_validation_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            flow_id=flow_id,
            bulk_run_id=bulk_run_id,
            template_url=self.send_policy_validation_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PolicyValidationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    send_policy_validation_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/FlowRunsAdmin/{flowId}/bulkRuns/{bulkRunId}/policy'}  # type: ignore


    @distributed_trace_async
    async def check_policy_validation_async(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        flow_id: str,
        bulk_run_id: str,
        **kwargs: Any
    ) -> "_models.PolicyValidationResponse":
        """check_policy_validation_async.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param flow_id:
        :type flow_id: str
        :param bulk_run_id:
        :type bulk_run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyValidationResponse, or the result of cls(response)
        :rtype: ~flow.models.PolicyValidationResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyValidationResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_check_policy_validation_async_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            flow_id=flow_id,
            bulk_run_id=bulk_run_id,
            template_url=self.check_policy_validation_async.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PolicyValidationResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_policy_validation_async.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/FlowRunsAdmin/{flowId}/bulkRuns/{bulkRunId}/policy'}  # type: ignore


    @distributed_trace_async
    async def log_result_for_bulk_run(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        flow_id: str,
        bulk_run_id: str,
        **kwargs: Any
    ) -> List["_models.KeyValuePairStringObject"]:
        """log_result_for_bulk_run.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :param flow_id:
        :type flow_id: str
        :param bulk_run_id:
        :type bulk_run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of KeyValuePairStringObject, or the result of cls(response)
        :rtype: list[~flow.models.KeyValuePairStringObject]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.KeyValuePairStringObject"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_log_result_for_bulk_run_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            flow_id=flow_id,
            bulk_run_id=bulk_run_id,
            template_url=self.log_result_for_bulk_run.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('[KeyValuePairStringObject]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    log_result_for_bulk_run.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/FlowRunsAdmin/{flowId}/bulkRuns/{bulkRunId}/LogResult'}  # type: ignore


    @distributed_trace_async
    async def get_storage_info(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        **kwargs: Any
    ) -> "_models.StorageInfo":
        """get_storage_info.

        :param subscription_id: The Azure Subscription ID.
        :type subscription_id: str
        :param resource_group_name: The Name of the resource group in which the workspace is located.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageInfo, or the result of cls(response)
        :rtype: ~flow.models.StorageInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StorageInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_storage_info_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            template_url=self.get_storage_info.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('StorageInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_storage_info.metadata = {'url': '/flow/api/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/FlowRunsAdmin/storageInfo'}  # type: ignore

