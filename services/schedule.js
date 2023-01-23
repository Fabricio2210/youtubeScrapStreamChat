const cron = require("node-cron");
const script = require("./runScript");

const streamSchedule = (timeStart) => {
    cron.schedule(
      timeStart,
      () => {
        script();
      },
      {
        scheduled: true,
        timezone: "America/Los_Angeles",
      }
    );
  };
  
  module.exports = streamSchedule;