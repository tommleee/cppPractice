package reportCard;

public class Student {

	private Class class1;
	private Class class2;
	private Class class3;
	private Class class4;
	
	public Class getClass1() {
		return class1;
	}


	public void setClass1(Class class1) {
		this.class1 = class1;
	}


	public Class getClass2() {
		return class2;
	}


	public void setClass2(Class class2) {
		this.class2 = class2;
	}


	public Class getClass3() {
		return class3;
	}


	public void setClass3(Class class3) {
		this.class3 = class3;
	}


	public Class getClass4() {
		return class4;
	}


	public void setClass4(Class class4) {
		this.class4 = class4;
	}
	
	public double calcGPA(Class c1, Class c2, Class c3, Class c4) {
		double gpa = (c1.getGradePoint() + c2.getGradePoint() + c3.getGradePoint() + c4.getGradePoint()) / 4;
		return gpa;
	}
	
	public Student() {
	}
	
	public Student(Class class1, Class class2, Class class3, Class class4) {
		this.class1 = class1;
		this.class2 = class2;
		this.class3 = class3;
		this.class4 = class4;
	}
	
	public String toString() {
		return "Student is taking " + this.class1.getSubject() + ", " + this.class2.getSubject() + ", " + this.class3.getSubject() + ", " + this.class4.getSubject() + 
			   "\nwith the GPA of " + this.calcGPA(this.getClass1(), this.getClass2(), this.getClass3(), this.getClass4()) + ".";
	}
}
