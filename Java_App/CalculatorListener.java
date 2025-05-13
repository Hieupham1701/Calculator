package Controller;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import View.CalculatorView;

public class CalculatorListener implements ActionListener {
	private CalculatorView cv;

	public CalculatorListener(CalculatorView cv) {
		this.cv = cv;
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		String src = e.getActionCommand();
		if (src.equals("+")) {this.cv.plus();}
		if (src.equals("-")) {this.cv.minus();}
		if (src.equals("*")){this.cv.multiply();}
		if (src.equals("/")){this.cv.divide();}
		if (src.equals("%")){this.cv.mod();}
		if (src.equals("^")){this.cv.pow();}
		
	}

}
