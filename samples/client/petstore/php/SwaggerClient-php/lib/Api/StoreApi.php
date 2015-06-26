<?php
/**
 *  Copyright 2015 SmartBear Software
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

/**
 *
 * NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
 */

namespace Swagger\Client\Api;

use \Swagger\Client\Configuration;
use \Swagger\Client\ApiClient;
use \Swagger\Client\ApiException;
use \Swagger\Client\ObjectSerializer;

class StoreApi {

  /** @var \Swagger\Client\ApiClient instance of the ApiClient */
  private $apiClient;

  /**
   * @param \Swagger\Client\ApiClient|null $apiClient The api client to use
   */
  function __construct($apiClient = null) {
    if ($apiClient == null) {
      $apiClient = new ApiClient();
      $apiClient->getConfig()->setHost('http://petstore.swagger.io/v2');
    }

    $this->apiClient = $apiClient;
  }

  /**
   * @return \Swagger\Client\ApiClient get the API client
   */
  public function getApiClient() {
    return $this->apiClient;
  }

  /**
   * @param \Swagger\Client\ApiClient $apiClient set the API client
   * @return StoreApi
   */
  public function setApiClient(ApiClient $apiClient) {
    $this->apiClient = $apiClient;
    return $this;
  }

  
  /**
   * getInventory
   *
   * Returns pet inventories by status
   *
   * @return map[string,int]
   * @throws \Swagger\Client\ApiException on non-2xx response
   */
   public function getInventory() {
      

      // parse inputs
      $resourcePath = "/store/inventory";
      $resourcePath = str_replace("{format}", "json", $resourcePath);
      $method = "GET";
      $httpBody = '';
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $_header_accept = ApiClient::selectHeaderAccept(array('application/json', 'application/xml'));
      if (!is_null($_header_accept)) {
        $headerParams['Accept'] = $_header_accept;
      }
      $headerParams['Content-Type'] = ApiClient::selectHeaderContentType(array());

      
      
      
      
      

      // for model (json/xml)
      if (isset($_tempBody)) {
        $httpBody = $_tempBody; // $_tempBody is the method argument, if present
      } else if (count($formParams) > 0) {
        // for HTTP post (form)
        $httpBody = $formParams;
      }
      
      $apiKey = $this->apiClient->getApiKeyWithPrefix('api_key');
      if (isset($apiKey)) {
        $headerParams['api_key'] = $apiKey;
      }
      
      
      
      // make the API Call
      try {
        $response = $this->apiClient->callApi($resourcePath, $method,
                                              $queryParams, $httpBody,
                                              $headerParams, 'map[string,int]');
      } catch (ApiException $e) {
        switch ($e->getCode()) { 
          case 200:
            $data = $this->apiClient->getSerializer()->deserialize($e->getResponseBody(), 'map[string,int]', $httpHeader);
            $e->setResponseObject($data);
            break;
        }

        throw $e;
      }
      
      if (!$response) {
        return null;
      }

      $responseObject = $this->apiClient->getSerializer()->deserialize($response,'map[string,int]');
      return $responseObject;
      
  }
  
  /**
   * placeOrder
   *
   * Place an order for a pet
   *
   * @param \Swagger\Client\Model\Order $body order placed for purchasing the pet (required)
   * @return \Swagger\Client\Model\Order
   * @throws \Swagger\Client\ApiException on non-2xx response
   */
   public function placeOrder($body) {
      

      // parse inputs
      $resourcePath = "/store/order";
      $resourcePath = str_replace("{format}", "json", $resourcePath);
      $method = "POST";
      $httpBody = '';
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $_header_accept = ApiClient::selectHeaderAccept(array('application/json', 'application/xml'));
      if (!is_null($_header_accept)) {
        $headerParams['Accept'] = $_header_accept;
      }
      $headerParams['Content-Type'] = ApiClient::selectHeaderContentType(array());

      
      
      
      
      // body params
      $_tempBody = null;
      if (isset($body)) {
        $_tempBody = $body;
      }

      // for model (json/xml)
      if (isset($_tempBody)) {
        $httpBody = $_tempBody; // $_tempBody is the method argument, if present
      } else if (count($formParams) > 0) {
        // for HTTP post (form)
        $httpBody = $formParams;
      }
      
      // make the API Call
      try {
        $response = $this->apiClient->callApi($resourcePath, $method,
                                              $queryParams, $httpBody,
                                              $headerParams, '\Swagger\Client\Model\Order');
      } catch (ApiException $e) {
        switch ($e->getCode()) { 
          case 200:
            $data = $this->apiClient->getSerializer()->deserialize($e->getResponseBody(), '\Swagger\Client\Model\Order', $httpHeader);
            $e->setResponseObject($data);
            break;
        }

        throw $e;
      }
      
      if (!$response) {
        return null;
      }

      $responseObject = $this->apiClient->getSerializer()->deserialize($response,'\Swagger\Client\Model\Order');
      return $responseObject;
      
  }
  
  /**
   * getOrderById
   *
   * Find purchase order by ID
   *
   * @param string $order_id ID of pet that needs to be fetched (required)
   * @return \Swagger\Client\Model\Order
   * @throws \Swagger\Client\ApiException on non-2xx response
   */
   public function getOrderById($order_id) {
      
      // verify the required parameter 'order_id' is set
      if ($order_id === null) {
        throw new \InvalidArgumentException('Missing the required parameter $order_id when calling getOrderById');
      }
      

      // parse inputs
      $resourcePath = "/store/order/{orderId}";
      $resourcePath = str_replace("{format}", "json", $resourcePath);
      $method = "GET";
      $httpBody = '';
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $_header_accept = ApiClient::selectHeaderAccept(array('application/json', 'application/xml'));
      if (!is_null($_header_accept)) {
        $headerParams['Accept'] = $_header_accept;
      }
      $headerParams['Content-Type'] = ApiClient::selectHeaderContentType(array());

      
      
      // path params
      if($order_id !== null) {
        $resourcePath = str_replace("{" . "orderId" . "}",
                                    $this->apiClient->getSerializer()->toPathValue($order_id),
                                    $resourcePath);
      }
      
      

      // for model (json/xml)
      if (isset($_tempBody)) {
        $httpBody = $_tempBody; // $_tempBody is the method argument, if present
      } else if (count($formParams) > 0) {
        // for HTTP post (form)
        $httpBody = $formParams;
      }
      
      // make the API Call
      try {
        $response = $this->apiClient->callApi($resourcePath, $method,
                                              $queryParams, $httpBody,
                                              $headerParams, '\Swagger\Client\Model\Order');
      } catch (ApiException $e) {
        switch ($e->getCode()) { 
          case 200:
            $data = $this->apiClient->getSerializer()->deserialize($e->getResponseBody(), '\Swagger\Client\Model\Order', $httpHeader);
            $e->setResponseObject($data);
            break;
        }

        throw $e;
      }
      
      if (!$response) {
        return null;
      }

      $responseObject = $this->apiClient->getSerializer()->deserialize($response,'\Swagger\Client\Model\Order');
      return $responseObject;
      
  }
  
  /**
   * deleteOrder
   *
   * Delete purchase order by ID
   *
   * @param string $order_id ID of the order that needs to be deleted (required)
   * @return void
   * @throws \Swagger\Client\ApiException on non-2xx response
   */
   public function deleteOrder($order_id) {
      
      // verify the required parameter 'order_id' is set
      if ($order_id === null) {
        throw new \InvalidArgumentException('Missing the required parameter $order_id when calling deleteOrder');
      }
      

      // parse inputs
      $resourcePath = "/store/order/{orderId}";
      $resourcePath = str_replace("{format}", "json", $resourcePath);
      $method = "DELETE";
      $httpBody = '';
      $queryParams = array();
      $headerParams = array();
      $formParams = array();
      $_header_accept = ApiClient::selectHeaderAccept(array('application/json', 'application/xml'));
      if (!is_null($_header_accept)) {
        $headerParams['Accept'] = $_header_accept;
      }
      $headerParams['Content-Type'] = ApiClient::selectHeaderContentType(array());

      
      
      // path params
      if($order_id !== null) {
        $resourcePath = str_replace("{" . "orderId" . "}",
                                    $this->apiClient->getSerializer()->toPathValue($order_id),
                                    $resourcePath);
      }
      
      

      // for model (json/xml)
      if (isset($_tempBody)) {
        $httpBody = $_tempBody; // $_tempBody is the method argument, if present
      } else if (count($formParams) > 0) {
        // for HTTP post (form)
        $httpBody = $formParams;
      }
      
      // make the API Call
      try {
        $response = $this->apiClient->callApi($resourcePath, $method,
                                              $queryParams, $httpBody,
                                              $headerParams);
      } catch (ApiException $e) {
        switch ($e->getCode()) { 
        }

        throw $e;
      }
      
  }
  
}
