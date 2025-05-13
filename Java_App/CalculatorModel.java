package Model;

public class CalculatorModel {
	private double firstvalue;
	private double secondvalue;
	private double answer;
	public CalculatorModel() {
		
	}
	public double getFirstvalue() {
		return firstvalue;
	}
	public void setFirstvalue(double firstvalue) {
		this.firstvalue = firstvalue;
	}
	public double getSecondvalue() {
		return secondvalue;
	}
	public void setSecondvalue(double secondvalue) {
		this.secondvalue = secondvalue;
	}
	public double getAnswer() {
		return answer;
	}
	public void setAnswer(double answer) {
		this.answer = answer;
	}
	public void plus() {
		this.answer = this.firstvalue + this.secondvalue;
	}
	public void minus() {
		this.answer = this.firstvalue - this.secondvalue;
	}
	public void multiply() {
		this.answer = this.firstvalue * this.secondvalue;
	}
	public void divide(){
		this.answer = this.firstvalue / this.secondvalue;
	}
	public void pow() {
		this.answer = Math.pow(this.firstvalue,this.secondvalue);
	}
	public void mod() {
		this.answer = this.firstvalue % this.secondvalue;
	}
	

}
