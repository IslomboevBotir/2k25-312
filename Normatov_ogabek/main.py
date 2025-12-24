from core.controller import CityController

def main():
    controller = CityController.get_instance()
    controller.start_console()

if __name__ == '__main__':
    main()
