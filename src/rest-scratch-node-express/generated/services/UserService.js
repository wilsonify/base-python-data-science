/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Create user
* This can only be done by the logged in user.
*
* body User Created user object
* no response value expected for this operation
* */
const create_user = ({ body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Creates list of users with given input array
*
* body List List of user object
* no response value expected for this operation
* */
const create_users_with_array_input = ({ body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Creates list of users with given input array
*
* body List List of user object
* no response value expected for this operation
* */
const create_users_with_list_input = ({ body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Delete user
* This can only be done by the logged in user.
*
* username String The name that needs to be deleted
* no response value expected for this operation
* */
const delete_user = ({ username }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        username,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Get user by user name
*
* username String The name that needs to be fetched. Use user1 for testing. 
* returns {username}
* */
const get_user_by_name = ({ username }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        username,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Logs user into the system
*
* username String The user name for login
* password String The password for login in clear text
* returns String
* */
const login_user = ({ username, password }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        username,
        password,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Logs out current logged in user session
*
* no response value expected for this operation
* */
const logout_user = () => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Updated user
* This can only be done by the logged in user.
*
* username String name that need to be updated
* body {username} Updated user object
* no response value expected for this operation
* */
const update_user = ({ username, body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        username,
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

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
