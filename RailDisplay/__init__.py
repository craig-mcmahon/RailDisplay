from nredarwin.webservice import DarwinLdbSession

class RailDisplay:

    config = None
    service_count = 0
    journey_count = 0

    def __init__(self, config):
        self.config = config
        self.service_count = 0
        self.journey_count = 0
        self.darwin_session = DarwinLdbSession(wsdl=config["wsdl"], api_key=config["api_key"])
        self.board = None
        self.displays = []
        # Configure displays
        for display_config in config['displays']:
            # Skip if not enabled
            if display_config['enabled']:
                # Create and store instance
                class_name = display_config['class']
                display_module = __import__('RailDisplay.Display.%s' % class_name, fromlist=["RailDisplay.Display"])
                display_class = getattr(display_module, class_name)
                self.displays.append(display_class(config=display_config, rail=self))

    # Update the board
    def update_board(self):
        from_csr = self.config["journey"][self.journey_count]["departure_station"]
        to_csr = self.config["journey"][self.journey_count]["destination_station"]
        self.board = self.darwin_session.get_station_board(from_csr, 10, True, False, to_csr)
        print 'Updating Board'
        self.display_train(self.service_count)

    # Display train details on all configured displays
    def display_train(self, count):
        s = self.board.train_services[count]
        message = s.destination_text + " - " + s.std + " - " + s.etd
        for display in self.displays:
            display.display_message(message)
        # If the train is late, let the display alert
        if s.etd != 'On time':
            for display in self.displays:
                display.alert_late()
