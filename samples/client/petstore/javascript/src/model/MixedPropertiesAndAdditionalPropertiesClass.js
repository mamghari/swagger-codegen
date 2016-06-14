(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/Animal'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./Animal'));
  } else {
    // Browser globals (root is window)
    if (!root.SwaggerPetstore) {
      root.SwaggerPetstore = {};
    }
    root.SwaggerPetstore.MixedPropertiesAndAdditionalPropertiesClass = factory(root.SwaggerPetstore.ApiClient, root.SwaggerPetstore.Animal);
  }
}(this, function(ApiClient, Animal) {
  'use strict';




  /**
   * The MixedPropertiesAndAdditionalPropertiesClass model module.
   * @module model/MixedPropertiesAndAdditionalPropertiesClass
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>MixedPropertiesAndAdditionalPropertiesClass</code>.
   * @alias module:model/MixedPropertiesAndAdditionalPropertiesClass
   * @class
   */
  var exports = function() {
    var _this = this;




  };

  /**
   * Constructs a <code>MixedPropertiesAndAdditionalPropertiesClass</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/MixedPropertiesAndAdditionalPropertiesClass} obj Optional instance to populate.
   * @return {module:model/MixedPropertiesAndAdditionalPropertiesClass} The populated <code>MixedPropertiesAndAdditionalPropertiesClass</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('uuid')) {
        obj['uuid'] = ApiClient.convertToType(data['uuid'], 'String');
      }
      if (data.hasOwnProperty('dateTime')) {
        obj['dateTime'] = ApiClient.convertToType(data['dateTime'], 'Date');
      }
      if (data.hasOwnProperty('map')) {
        obj['map'] = ApiClient.convertToType(data['map'], {'String': Animal});
      }
    }
    return obj;
  }

  /**
   * @member {String} uuid
   */
  exports.prototype['uuid'] = undefined;
  /**
   * @member {Date} dateTime
   */
  exports.prototype['dateTime'] = undefined;
  /**
   * @member {Object.<String, module:model/Animal>} map
   */
  exports.prototype['map'] = undefined;




  return exports;
}));


