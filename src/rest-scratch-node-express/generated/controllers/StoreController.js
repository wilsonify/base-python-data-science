/**
 * The StoreController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic routes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/StoreService');
const delete_order = async (request, response) => {
  await Controller.handleRequest(request, response, service.delete_order);
};

const get_inventory = async (request, response) => {
  await Controller.handleRequest(request, response, service.get_inventory);
};

const get_order_by_id = async (request, response) => {
  await Controller.handleRequest(request, response, service.get_order_by_id);
};

const place_order = async (request, response) => {
  await Controller.handleRequest(request, response, service.place_order);
};


module.exports = {
  delete_order,
  get_inventory,
  get_order_by_id,
  place_order,
};
