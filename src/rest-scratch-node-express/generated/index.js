const config = require('./config');
const logger = require('./logger');
const ExpressServer = require('./expressServer');

const launchServer = async () => {
  console.log(`__dirname = ${__dirname}`)
  console.log(`config.OPENAPI_YAML = ${config.OPENAPI_YAML}`)
  this.expressServer = new ExpressServer(config.URL_PORT, config.OPENAPI_YAML);
  this.expressServer.launch();
  logger.info('Express server running');
};

launchServer().catch(e => logger.error(e));
