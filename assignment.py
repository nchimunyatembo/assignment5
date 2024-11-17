// assignment 1

public class Smartphone {
    private String brand;
    private String model;
    private int storageCapacity;
    private String operatingSystem;

    // Constructor to initialize the smartphone object
    public Smartphone(String brand, String model, int storageCapacity, String operatingSystem) {
        this.brand = brand;
        this.model = model;
        this.storageCapacity = storageCapacity;
        this.operatingSystem = operatingSystem;
    }

    // Method to display smartphone information
    public void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Storage Capacity: " + storageCapacity + "GB");
        System.out.println("Operating System: " + operatingSystem);
    }

    // Method to simulate making a call
    public void makeCall(String phoneNumber) {
        System.out.println("Calling " + phoneNumber + "...");
    }

    // Method to simulate sending a text message
    public void sendMessage(String phoneNumber, String message) {
        System.out.println("Sending message to " + phoneNumber + ": " + message);
    }
}

// Inherited class: SmartPhone with Camera
class SmartPhoneWithCamera extends Smartphone {
    private int cameraResolution;

    // Constructor to initialize the smartphone with camera object
    public SmartPhoneWithCamera(String brand, String model, int storageCapacity, String operatingSystem, int cameraResolution) {
        super(brand, model, storageCapacity, operatingSystem);
        this.cameraResolution = cameraResolution;
    }

    // Overridden method to display additional camera information
    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Camera Resolution: " + cameraResolution + "MP");
    }

    // Method to simulate taking a photo
    public void takePhoto() {
        System.out.println("Capturing image with " + cameraResolution + "MP camera...");
    }
}

//assignment 2

interface Movable {
    void move();
}

class Car implements Movable {
    @Override
    public void move() {
        System.out.println("Driving 🚗");
    }
}

class Plane implements Movable {
    @Override
    public void move() {
        System.out.println("Flying ✈️");
    }
}

class Dog implements Movable {
    @Override
    public void move() {
        System.out.println("Running 🐶");
    }
}

public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        Plane plane = new Plane();
        Dog dog = new Dog();

        car.move();
        plane.move();
        dog.move();
    }
}