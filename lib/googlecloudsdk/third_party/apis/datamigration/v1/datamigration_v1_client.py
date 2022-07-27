"""Generated client library for datamigration version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.datamigration.v1 import datamigration_v1_messages as messages


class DatamigrationV1(base_api.BaseApiClient):
  """Generated client library for service datamigration version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://datamigration.googleapis.com/'
  MTLS_BASE_URL = 'https://datamigration.mtls.googleapis.com/'

  _PACKAGE = 'datamigration'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DatamigrationV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new datamigration handle."""
    url = url or self.BASE_URL
    super(DatamigrationV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_connectionProfiles = self.ProjectsLocationsConnectionProfilesService(self)
    self.projects_locations_migrationJobs = self.ProjectsLocationsMigrationJobsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsConnectionProfilesService(base_api.BaseApiService):
    """Service class for the projects_locations_connectionProfiles resource."""

    _NAME = 'projects_locations_connectionProfiles'

    def __init__(self, client):
      super(DatamigrationV1.ProjectsLocationsConnectionProfilesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new connection profile in a given project and location.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles',
        http_method='POST',
        method_id='datamigration.projects.locations.connectionProfiles.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['connectionProfileId', 'requestId'],
        relative_path='v1/{+parent}/connectionProfiles',
        request_field='connectionProfile',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}',
        http_method='DELETE',
        method_id='datamigration.projects.locations.connectionProfiles.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force', 'requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single connection profile.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ConnectionProfile) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}',
        http_method='GET',
        method_id='datamigration.projects.locations.connectionProfiles.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesGetRequest',
        response_type_name='ConnectionProfile',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}:getIamPolicy',
        http_method='GET',
        method_id='datamigration.projects.locations.connectionProfiles.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Retrieves a list of all connection profiles in a given project and location.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectionProfilesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles',
        http_method='GET',
        method_id='datamigration.projects.locations.connectionProfiles.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/connectionProfiles',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesListRequest',
        response_type_name='ListConnectionProfilesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update the configuration of a single connection profile.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}',
        http_method='PATCH',
        method_id='datamigration.projects.locations.connectionProfiles.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='connectionProfile',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}:setIamPolicy',
        http_method='POST',
        method_id='datamigration.projects.locations.connectionProfiles.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (DatamigrationProjectsLocationsConnectionProfilesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/connectionProfiles/{connectionProfilesId}:testIamPermissions',
        http_method='POST',
        method_id='datamigration.projects.locations.connectionProfiles.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='DatamigrationProjectsLocationsConnectionProfilesTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsMigrationJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_migrationJobs resource."""

    _NAME = 'projects_locations_migrationJobs'

    def __init__(self, client):
      super(DatamigrationV1.ProjectsLocationsMigrationJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new migration job in a given project and location.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['migrationJobId', 'requestId'],
        relative_path='v1/{+parent}/migrationJobs',
        request_field='migrationJob',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single migration job.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}',
        http_method='DELETE',
        method_id='datamigration.projects.locations.migrationJobs.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force', 'requestId'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def GenerateSshScript(self, request, global_params=None):
      r"""Generate a SSH configuration script to configure the reverse SSH connectivity.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsGenerateSshScriptRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SshScript) The response message.
      """
      config = self.GetMethodConfig('GenerateSshScript')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateSshScript.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:generateSshScript',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.generateSshScript',
        ordered_params=['migrationJob'],
        path_params=['migrationJob'],
        query_params=[],
        relative_path='v1/{+migrationJob}:generateSshScript',
        request_field='generateSshScriptRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsGenerateSshScriptRequest',
        response_type_name='SshScript',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single migration job.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (MigrationJob) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}',
        http_method='GET',
        method_id='datamigration.projects.locations.migrationJobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsGetRequest',
        response_type_name='MigrationJob',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:getIamPolicy',
        http_method='GET',
        method_id='datamigration.projects.locations.migrationJobs.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists migration jobs in a given project and location.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListMigrationJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs',
        http_method='GET',
        method_id='datamigration.projects.locations.migrationJobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/migrationJobs',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsListRequest',
        response_type_name='ListMigrationJobsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single migration job.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}',
        http_method='PATCH',
        method_id='datamigration.projects.locations.migrationJobs.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1/{+name}',
        request_field='migrationJob',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Promote(self, request, global_params=None):
      r"""Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsPromoteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Promote')
      return self._RunMethod(
          config, request, global_params=global_params)

    Promote.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:promote',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.promote',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:promote',
        request_field='promoteMigrationJobRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsPromoteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Restart(self, request, global_params=None):
      r"""Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsRestartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Restart')
      return self._RunMethod(
          config, request, global_params=global_params)

    Restart.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:restart',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.restart',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:restart',
        request_field='restartMigrationJobRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsRestartRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Resume(self, request, global_params=None):
      r"""Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsResumeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Resume')
      return self._RunMethod(
          config, request, global_params=global_params)

    Resume.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:resume',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.resume',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:resume',
        request_field='resumeMigrationJobRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsResumeRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:setIamPolicy',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def Start(self, request, global_params=None):
      r"""Start an already created migration job.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsStartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Start')
      return self._RunMethod(
          config, request, global_params=global_params)

    Start.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:start',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.start',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:start',
        request_field='startMigrationJobRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsStartRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Stops a running migration job.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:stop',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.stop',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:stop',
        request_field='stopMigrationJobRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsStopRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:testIamPermissions',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

    def Verify(self, request, global_params=None):
      r"""Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.

      Args:
        request: (DatamigrationProjectsLocationsMigrationJobsVerifyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Verify')
      return self._RunMethod(
          config, request, global_params=global_params)

    Verify.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/migrationJobs/{migrationJobsId}:verify',
        http_method='POST',
        method_id='datamigration.projects.locations.migrationJobs.verify',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:verify',
        request_field='verifyMigrationJobRequest',
        request_type_name='DatamigrationProjectsLocationsMigrationJobsVerifyRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(DatamigrationV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (DatamigrationProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='datamigration.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='DatamigrationProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (DatamigrationProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='datamigration.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (DatamigrationProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='datamigration.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (DatamigrationProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='datamigration.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(DatamigrationV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (DatamigrationProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='datamigration.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (DatamigrationProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='datamigration.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/locations',
        request_field='',
        request_type_name='DatamigrationProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(DatamigrationV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
