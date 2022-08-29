/**
 * The PetController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic routes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/PetService');
const add_pet = async (request, response) => {
  await Controller.handleRequest(request, response, service.add_pet);
};

const delete_pet = async (request, response) => {
  await Controller.handleRequest(request, response, service.delete_pet);
};

const find_pets_by_status = async (request, response) => {
  await Controller.handleRequest(request, response, service.find_pets_by_status);
};

const find_pets_by_tags = async (request, response) => {
  await Controller.handleRequest(request, response, service.find_pets_by_tags);
};

const get_pet_by_id = async (request, response) => {
  await Controller.handleRequest(request, response, service.get_pet_by_id);
};

const update_pet = async (request, response) => {
  await Controller.handleRequest(request, response, service.update_pet);
};

const update_pet_with_form = async (request, response) => {
  await Controller.handleRequest(request, response, service.update_pet_with_form);
};

const upload_file = async (request, response) => {
  await Controller.handleRequest(request, response, service.upload_file);
};


module.exports = {
  add_pet,
  delete_pet,
  find_pets_by_status,
  find_pets_by_tags,
  get_pet_by_id,
  update_pet,
  update_pet_with_form,
  upload_file,
};
