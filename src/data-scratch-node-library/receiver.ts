var amqp = require('amqplib/callback_api');
var basename = require('path').basename;
var exopts = {durable: false};

function bail(err, conn) {
  console.error(err);
  if (conn) conn.close(function() { process.exit(1); });
}

function callerback(msg) {
    console.log(" [x] %s:'%s'",
                msg.fields.routingKey,
                msg.content.toString());
  }  

function on_connect(err, conn) {
  if (err !== null) return bail(err);
  process.once('SIGINT', function() { conn.close(); });
  conn.createChannel(function(err, ch) {
    if (err !== null) return bail(err, conn);    
    ch.assertExchange("dsnl-try", 'topic', exopts);
    ch.assertQueue('dsnl-try', {exclusive: true}, function(err, ok) {
      if (err !== null) return bail(err, conn);
      var queue = ok.queue
      function sub(err) {
        if (err !== null) return bail(err, conn);
        else {
            ch.bindQueue("dsnl-try", "dsnl-try", "dsnl", {}, sub);
        }
      }
      ch.consume(queue, callerback, {noAck: true}, function(err) {
        if (err !== null) return bail(err, conn);
        console.log(' [*] Waiting for logs. To exit press CTRL+C.');
        sub(null);
      });
    });
  });
}

amqp.connect(on_connect);
