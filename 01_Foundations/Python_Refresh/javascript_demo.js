/**
 * JavaScript Demo Script
 * A comprehensive demonstration of JavaScript features and best practices.
 */

// 1. Enums (using Object.freeze)
const Color = Object.freeze({
    RED: 1,
    GREEN: 2,
    BLUE: 3
});

// 2. Classes
class Person {
    constructor(name, age, email = null) {
        this.name = name;
        this.age = age;
        this.email = email;
    }

    toString() {
        return `Person(name=${this.name}, age=${this.age}, email=${this.email})`;
    }
}

// 3. Abstract Class (using a base class)
class Shape {
    area() {
        throw new Error('Method area() must be implemented');
    }

    perimeter() {
        throw new Error('Method perimeter() must be implemented');
    }
}

// 4. Concrete Class
class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    area() {
        return Math.PI * this.radius ** 2;
    }

    perimeter() {
        return 2 * Math.PI * this.radius;
    }
}

// 5. Decorator (using a higher-order function)
function timer(func) {
    return function(...args) {
        const start = performance.now();
        const result = func.apply(this, args);
        const end = performance.now();
        console.log(`${func.name} took ${(end - start).toFixed(2)}ms to execute`);
        return result;
    };
}

// 6. File Operations (using Node.js fs promises)
const fs = require('fs').promises;

class FileHandler {
    static async writeFile(filename, content) {
        try {
            await fs.writeFile(filename, content);
            console.log(`Successfully wrote to ${filename}`);
        } catch (error) {
            console.error(`Error writing to file: ${error.message}`);
        }
    }
}

// 7. Generator Function
function* fibonacci(n) {
    let [a, b] = [0, 1];
    for (let i = 0; i < n; i++) {
        yield a;
        [a, b] = [b, a + b];
    }
}

// 8. Modern JavaScript Features
const processData = (data) => {
    return {
        count: data.length,
        total: data.reduce((sum, item) => sum + (item.value || 0), 0),
        average: data.length ? 
            data.reduce((sum, item) => sum + (item.value || 0), 0) / data.length : 0
    };
};

// 9. Async Function
async function asyncOperation() {
    await new Promise(resolve => setTimeout(resolve, 1000));
    return "Async operation completed";
}

// 10. Main Function with Examples
async function main() {
    // Demonstrate Enum
    console.log(`Color.RED: ${Color.RED}`);

    // Demonstrate Class
    const person = new Person("John Doe", 30, "john@example.com");
    console.log(`Person: ${person}`);

    // Demonstrate Class Inheritance
    const circle = new Circle(5);
    console.log(`Circle area: ${circle.area().toFixed(2)}`);
    console.log(`Circle perimeter: ${circle.perimeter().toFixed(2)}`);

    // Demonstrate Generator
    console.log("Fibonacci sequence:");
    for (const num of fibonacci(5)) {
        console.log(num);
    }

    // Demonstrate File Operations
    await FileHandler.writeFile("demo.txt", "Hello, JavaScript!");

    // Demonstrate Data Processing
    const data = [
        { value: 10 },
        { value: 20 },
        { value: 30 }
    ];
    const result = processData(data);
    console.log(`Processed data:`, result);

    // Demonstrate JSON Operations
    const jsonData = JSON.stringify(result, null, 2);
    console.log(`JSON data:\n${jsonData}`);

    // Demonstrate Async Operation
    const asyncResult = await asyncOperation();
    console.log(asyncResult);
}

// Run the main function
main().catch(console.error); 