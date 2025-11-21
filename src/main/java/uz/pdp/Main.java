package uz.pdp;

import uz.pdp.core.SmartCityController;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        SmartCityController controller = SmartCityController.getInstance();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the SmartCity Management System!");

        while (true) {
            System.out.println("""
                    \nPlease select an option:
                    1. Get Full City Status Report
                    2. Activate Night Mode (Lights ON, Security ARMED)
                    3. Activate Day Mode (Lights OFF)
                    4. Trigger Emergency Protocol
                    5. Disarm Security System (Admin)
                    0. Exit
                    """);
            System.out.print("Enter choice: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
                continue;
            }

            switch (choice) {
                case 1 -> controller.reportFullStatus();
                case 2 -> controller.activateNightMode();
                case 3 -> controller.activateDayMode();
                case 4 -> {
                    System.out.print("Enter emergency location: ");
                    String location = scanner.nextLine();
                    controller.triggerEmergency(location);
                }
                case 5 -> {
                    System.out.print("Enter admin password to disarm security: ");
                    String password = scanner.nextLine();
                    controller.disarmSecurity(password);
                }
                case 0 -> {
                    System.out.println("Exiting SmartCity System. Goodbye!");
                    scanner.close();
                    return;
                }
                default -> System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
