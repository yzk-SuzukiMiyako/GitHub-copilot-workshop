function calculateSum(a, b) {
   // ここで実装を中断
    return a + b;
}

// JavaScript で Student クラスを作成
// プロパティ: name, age, grade
// メソッド: getInfo() - 学生情報を文字列で返す
// メソッド: isAdult() - 18歳以上かどうかを返す
class Student {
    constructor(name, age, grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }
    getInfo() {
        return `Name: ${this.name}, Age: ${this.age}, Grade: ${this.grade}`;
    }
    isAdult() {
        return this.age >= 18;
    }
}
