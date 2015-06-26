<?php
require_once(__DIR__ . '/SwaggerClient-php/autoload.php');

// show error reporting
//ini_set('display_errors', 1);
//error_reporting(~0);

// initialize the API client
//$api_client = new SwaggerClient\ApiClient('http://petstore.swagger.io/v2');
//$api_client->addDefaultHeader("test1", "value1");

// to enable logging
//SwaggerClient\Configuration::$debug = true;
//SwaggerClient\Configuration::$debug_file = '/var/tmp/php_debug.log';

$petId = 10005; // ID of pet that needs to be fetched
try {
    // get pet by id
    //$pet_api = new SwaggerClient\PetAPI($api_client);
    $pet_api = new Swagger\Client\Api\PetAPI();
    // test default header
    //$pet_api->getApiClient()->addDefaultHeader("TEST_API_KEY", "09182sdkanafndsl903");
    // return Pet (model)
    $response = $pet_api->getPetById($petId);
    // to test __toString()
    print ($response);

    // add pet (post json)
    $new_pet_id = 10005;
    $new_pet = new Swagger\Client\Model\Pet;
    $new_pet->setId($new_pet_id);
    $new_pet->setName("PHP Unit Test");
    // new tag
    $tag= new Swagger\Client\Model\Tag;
    $tag->setId($new_pet_id); // use the same id as pet
    //$tag->name = "test php tag";
    // new category
    $category = new Swagger\Client\Model\Category;
    $category->setId(10005); // use the same id as pet
    //$category->name = "test php category";

    $new_pet->setTags(array($tag));
    $new_pet->setCategory($category);

    $pet_api = new Swagger\Client\Api\PetAPI();
    // add a new pet (model)
    $add_response = $pet_api->addPet($new_pet);

    // test upload file (exception)
    //$upload_response = $pet_api->uploadFile($petId, "test meta", NULL);

} catch (Swagger\Client\Exception $e) {
    echo 'Caught exception: ', $e->getMessage(), "\n";
    echo 'HTTP response headers: ', $e->getResponseHeaders(), "\n";
    echo 'HTTP response body: ', $e->getResponseBody(), "\n";
    echo 'HTTP status code: ', $e->getCode(), "\n";
}
