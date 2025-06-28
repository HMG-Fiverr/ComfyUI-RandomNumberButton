app.registerExtension({
  name: "AgentAssist.RandomNumberButton",
  nodeCreated(node, app) {
    // Check if the node is our RandomNumberButton node
    if (node.type === "RandomNumberButton") {
      // Add a button widget
      const button = node.addWidget("button", "Generate", "generate_button", () => {
        // When the button is clicked, queue the prompt (run the workflow)
        app.queuePrompt();
      });
      // Optional: Make the button fill the width of the node
      button.serialize = false; // Don't save the button state in the workflow file
    }
  }
});