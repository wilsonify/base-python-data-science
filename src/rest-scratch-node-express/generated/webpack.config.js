// Generated using webpack-cli https://github.com/webpack/webpack-cli

const path = require("path");
const stylesHandler = "style-loader";

module.exports = {
  mode: 'development',
  entry: "./index.js",
  output: { path: path.resolve(__dirname, "dist"), filename: "index.js" },
  plugins: [
    // Add your plugins here from https://webpack.js.org/configuration/plugins/
  ],
  module: {
    rules: [
      { test: /\.(ts|tsx)$/i, loader: "ts-loader" },
      { test: /\.css$/i, use: [stylesHandler, "css-loader"] },
      { test: /\.(eot|svg|ttf|woff|woff2|png|jpg|gif)$/i, type: "asset", },
      // Add your rules for custom modules here from https://webpack.js.org/loaders/
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".jsx", ".js", "..."],
    fallback: {
      "fs": false,
      "tls": false,
      "net": false,
      "path": false,
      "zlib": false,
      "http": false,
      "https": false,
      "stream": false,
      "os": require.resolve("os-browserify/browser"),
      "util":false,
      "url":false,
      "crypto":false,
      "querystring": false
    }
  },
};