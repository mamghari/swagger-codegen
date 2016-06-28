# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class FakeApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def test_code_inject__end(self, **kwargs):
        """
        To test code injection */ =end
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_code_inject__end(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str test_code_inject__end: To test code injection */ =end
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_code_inject__end_with_http_info(**kwargs)
        else:
            (data) = self.test_code_inject__end_with_http_info(**kwargs)
            return data

    def test_code_inject__end_with_http_info(self, **kwargs):
        """
        To test code injection */ =end
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_code_inject__end_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str test_code_inject__end: To test code injection */ =end
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['test_code_inject__end']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_code_inject__end" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/fake'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'test_code_inject__end' in params:
            form_params.append(('test code inject */ &#x3D;end', params['test_code_inject__end']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', '*/ end'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', '*/ =end));(phpinfo('])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def test_endpoint_parameters(self, number, double, string, byte, **kwargs):
        """
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_endpoint_parameters(number, double, string, byte, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float number: None (required)
        :param float double: None (required)
        :param str string: None (required)
        :param str byte: None (required)
        :param int integer: None
        :param int int32: None
        :param int int64: None
        :param float float: None
        :param str binary: None
        :param date date: None
        :param datetime date_time: None
        :param str password: None
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_endpoint_parameters_with_http_info(number, double, string, byte, **kwargs)
        else:
            (data) = self.test_endpoint_parameters_with_http_info(number, double, string, byte, **kwargs)
            return data

    def test_endpoint_parameters_with_http_info(self, number, double, string, byte, **kwargs):
        """
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 
        Fake endpoint for testing various parameters 假端點 偽のエンドポイント 가짜 엔드 포인트 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_endpoint_parameters_with_http_info(number, double, string, byte, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float number: None (required)
        :param float double: None (required)
        :param str string: None (required)
        :param str byte: None (required)
        :param int integer: None
        :param int int32: None
        :param int int64: None
        :param float float: None
        :param str binary: None
        :param date date: None
        :param datetime date_time: None
        :param str password: None
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['number', 'double', 'string', 'byte', 'integer', 'int32', 'int64', 'float', 'binary', 'date', 'date_time', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_endpoint_parameters" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'number' is set
        if ('number' not in params) or (params['number'] is None):
            raise ValueError("Missing the required parameter `number` when calling `test_endpoint_parameters`")
        # verify the required parameter 'double' is set
        if ('double' not in params) or (params['double'] is None):
            raise ValueError("Missing the required parameter `double` when calling `test_endpoint_parameters`")
        # verify the required parameter 'string' is set
        if ('string' not in params) or (params['string'] is None):
            raise ValueError("Missing the required parameter `string` when calling `test_endpoint_parameters`")
        # verify the required parameter 'byte' is set
        if ('byte' not in params) or (params['byte'] is None):
            raise ValueError("Missing the required parameter `byte` when calling `test_endpoint_parameters`")

        if 'number' in params and params['number'] > 543.2:
            raise ValueError("Invalid value for parameter `number` when calling `test_endpoint_parameters`, must be a value less than or equal to  `543.2`")
        if 'number' in params and params['number'] < 32.1:
            raise ValueError("Invalid value for parameter `number` when calling `test_endpoint_parameters`, must be a value greater than or equal to `32.1`")
        if 'double' in params and params['double'] > 123.4:
            raise ValueError("Invalid value for parameter `double` when calling `test_endpoint_parameters`, must be a value less than or equal to  `123.4`")
        if 'double' in params and params['double'] < 67.8:
            raise ValueError("Invalid value for parameter `double` when calling `test_endpoint_parameters`, must be a value greater than or equal to `67.8`")
        if 'string' in params and not re.search('[a-z]', params['string'], flags=re.IGNORECASE):
            raise ValueError("Invalid value for parameter `string` when calling `test_endpoint_parameters`, must conform to the pattern `/[a-z]/i`")
        if 'integer' in params and params['integer'] > 100.0:
            raise ValueError("Invalid value for parameter `integer` when calling `test_endpoint_parameters`, must be a value less than or equal to  `100.0`")
        if 'integer' in params and params['integer'] < 10.0:
            raise ValueError("Invalid value for parameter `integer` when calling `test_endpoint_parameters`, must be a value greater than or equal to `10.0`")
        if 'int32' in params and params['int32'] > 200.0:
            raise ValueError("Invalid value for parameter `int32` when calling `test_endpoint_parameters`, must be a value less than or equal to  `200.0`")
        if 'int32' in params and params['int32'] < 20.0:
            raise ValueError("Invalid value for parameter `int32` when calling `test_endpoint_parameters`, must be a value greater than or equal to `20.0`")
        if 'float' in params and params['float'] > 987.6:
            raise ValueError("Invalid value for parameter `float` when calling `test_endpoint_parameters`, must be a value less than or equal to  `987.6`")
        if 'password' in params and len(params['password']) > 64:
            raise ValueError("Invalid value for parameter `password` when calling `test_endpoint_parameters`, length must be less than or equal to `64`")
        if 'password' in params and len(params['password']) < 10:
            raise ValueError("Invalid value for parameter `password` when calling `test_endpoint_parameters`, length must be greater than or equal to `10`")
        resource_path = '/fake'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'integer' in params:
            form_params.append(('integer', params['integer']))
        if 'int32' in params:
            form_params.append(('int32', params['int32']))
        if 'int64' in params:
            form_params.append(('int64', params['int64']))
        if 'number' in params:
            form_params.append(('number', params['number']))
        if 'float' in params:
            form_params.append(('float', params['float']))
        if 'double' in params:
            form_params.append(('double', params['double']))
        if 'string' in params:
            form_params.append(('string', params['string']))
        if 'byte' in params:
            form_params.append(('byte', params['byte']))
        if 'binary' in params:
            form_params.append(('binary', params['binary']))
        if 'date' in params:
            form_params.append(('date', params['date']))
        if 'date_time' in params:
            form_params.append(('dateTime', params['date_time']))
        if 'password' in params:
            form_params.append(('password', params['password']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml; charset=utf-8', 'application/json; charset=utf-8'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/xml; charset=utf-8', 'application/json; charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def test_enum_query_parameters(self, **kwargs):
        """
        To test enum query parameters
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_enum_query_parameters(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str enum_query_string: Query parameter enum test (string)
        :param float enum_query_integer: Query parameter enum test (double)
        :param float enum_query_double: Query parameter enum test (double)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_enum_query_parameters_with_http_info(**kwargs)
        else:
            (data) = self.test_enum_query_parameters_with_http_info(**kwargs)
            return data

    def test_enum_query_parameters_with_http_info(self, **kwargs):
        """
        To test enum query parameters
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_enum_query_parameters_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str enum_query_string: Query parameter enum test (string)
        :param float enum_query_integer: Query parameter enum test (double)
        :param float enum_query_double: Query parameter enum test (double)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enum_query_string', 'enum_query_integer', 'enum_query_double']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_enum_query_parameters" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/fake'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'enum_query_integer' in params:
            query_params['enum_query_integer'] = params['enum_query_integer']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'enum_query_string' in params:
            form_params.append(('enum_query_string', params['enum_query_string']))
        if 'enum_query_double' in params:
            form_params.append(('enum_query_double', params['enum_query_double']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
