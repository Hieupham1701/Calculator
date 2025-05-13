package View;

import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

import Controller.CalculatorListener;
import Model.CalculatorModel;

public class CalculatorView extends JFrame {
	private CalculatorModel calculator;
	private JTextField firstvaluetext;
	private JTextField secondvaluetext;
	private JTextField answervalue;
	public CalculatorView() {
		calculator = new CalculatorModel();
		this.init();
		this.setVisible(true);
		
	}
	public void init() {
		this.setTitle("My calculator");
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setSize(300,300);
		JLabel jlabel1 = new JLabel("1st value:");
		JLabel jlabel2 = new JLabel("2nd value:");
		JLabel jlabelanswer = new JLabel("Answer :");
		ActionListener ac = new CalculatorListener(this);
		Font font = new Font("Arial",Font.BOLD,20);
		jlabel1.setFont(font);
		jlabel2.setFont(font);
		jlabelanswer.setFont(font);
		firstvaluetext = new JTextField(20);
		secondvaluetext = new JTextField(20);
		answervalue = new JTextField(20);
		JPanel jpanel_inout = new JPanel(new GridLayout(3,2,10,10));
		jpanel_inout.add(jlabel1);
		jpanel_inout.add(firstvaluetext);
		jpanel_inout.add(jlabel2);
		jpanel_inout.add(secondvaluetext);
		jpanel_inout.add(jlabelanswer);
		jpanel_inout.add(answervalue);
		this.setLayout(new BorderLayout());
		this.add(jpanel_inout,BorderLayout.CENTER);
		JButton jbuttonplus = new JButton("+");
		jbuttonplus.setFont(font);
		jbuttonplus.addActionListener(ac);
		JButton jbuttonminus = new JButton("-");
		jbuttonminus.setFont(font);
		jbuttonminus.addActionListener(ac);
		JButton jbuttonmultiply = new JButton("*");
		jbuttonmultiply.setFont(font);
		jbuttonmultiply.addActionListener(ac);
		JButton jbuttondivide = new JButton("/");
		jbuttondivide.setFont(font);
		jbuttondivide.addActionListener(ac);
		JButton jbuttonmod = new JButton("%");
		jbuttonmod.setFont(font);
		jbuttonmod.addActionListener(ac);
		JButton jbuttonpow = new JButton("^");
		jbuttonpow.setFont(font);
		jbuttonpow.addActionListener(ac);
		JPanel jpanelbutton = new JPanel(new GridLayout(2,3));
		jpanelbutton.add(jbuttonplus);
		jpanelbutton.add(jbuttonminus);
		jpanelbutton.add(jbuttonmultiply);
		jpanelbutton.add(jbuttondivide);
		jpanelbutton.add(jbuttonmod);
		jpanelbutton.add(jbuttonpow);
		this.add(jpanelbutton,BorderLayout.SOUTH);
				
	}
	public void plus() {
		double first = Double.valueOf(firstvaluetext.getText());
		double second = Double.valueOf(secondvaluetext.getText());
		this.calculator.setFirstvalue(first);
		this.calculator.setSecondvalue(second);
		this.calculator.plus();
		this.answervalue.setText(this.calculator.getAnswer()+"");
	}
	public void minus() {
		double first = Double.valueOf(firstvaluetext.getText());
		double second = Double.valueOf(secondvaluetext.getText());
		this.calculator.setFirstvalue(first);
		this.calculator.setSecondvalue(second);
		this.calculator.minus();
		this.answervalue.setText(this.calculator.getAnswer()+"");
	}
	public void multiply() {
		double first = Double.valueOf(firstvaluetext.getText());
		double second = Double.valueOf(secondvaluetext.getText());
		this.calculator.setFirstvalue(first);
		this.calculator.setSecondvalue(second);
		this.calculator.multiply();
		this.answervalue.setText(this.calculator.getAnswer()+"");
	}
	public void divide() {
		double first = Double.valueOf(firstvaluetext.getText());
		double second = Double.valueOf(secondvaluetext.getText());
		this.calculator.setFirstvalue(first);
		this.calculator.setSecondvalue(second);
		this.calculator.divide();
		this.answervalue.setText(this.calculator.getAnswer()+"");
	}
	public void mod() {
		double first = Double.valueOf(firstvaluetext.getText());
		double second = Double.valueOf(secondvaluetext.getText());
		this.calculator.setFirstvalue(first);
		this.calculator.setSecondvalue(second);
		this.calculator.mod();
		this.answervalue.setText(this.calculator.getAnswer()+"");
	}
	public void pow() {
		double first = Double.valueOf(firstvaluetext.getText());
		double second = Double.valueOf(secondvaluetext.getText());
		this.calculator.setFirstvalue(first);
		this.calculator.setSecondvalue(second);
		this.calculator.pow();
		this.answervalue.setText(this.calculator.getAnswer()+"");
	}

}
