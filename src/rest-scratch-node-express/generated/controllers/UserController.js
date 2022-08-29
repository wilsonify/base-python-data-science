/**
 * The UserController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic routes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/UserService');
const create_user = async (request, response) => {
  await Controller.handleRequest(request, response, service.create_user);
};

const create_users_with_array_input = async (request, response) => {
  await Controller.handleRequest(request, response, service.create_users_with_array_input);
};

const create_users_with_list_input = async (request, response) => {
  await Controller.handleRequest(request, response, service.create_users_with_list_input);
};

const delete_user = async (request, response) => {
  await Controller.handleRequest(request, response, service.delete_user);
};

const get_user_by_name = async (request, response) => {
  await Controller.handleRequest(request, response, service.get_user_by_name);
};

const login_user = async (request, response) => {
  await Controller.handleRequest(request, response, service.login_user);
};

const logout_user = async (request, response) => {
  await Controller.handleRequest(request, response, service.logout_user);
};

const update_user = async (request, response) => {
  await Controller.handleRequest(request, response, service.update_user);
};


module.exports = {
  create_user,
  create_users_with_array_input,
  create_users_with_list_input,
  delete_user,
  get_user_by_name,
  login_user,
  logout_user,
  update_user,
};
