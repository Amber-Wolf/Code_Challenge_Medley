import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.TreeMap;

import javax.swing.text.html.HTMLDocument.Iterator;


public class Zplusminus {
	
	final int DEF = 0;
	final int FOR = 1;
	final int ENDFOR = 2;
	
	final int PLUS = 0;
	final int TIMES = 1;
	final int EQUALS = 2;
	
	final int END = -1;
	final int CHECKSEMICOLON = 0;
	final int FOREGOSEMICOLON = 1;
	
	String filename;
	String keyWords[] = {"DEF","FOR","ENDFOR"};
	String operators[] = {"+=", "*=", "="};
	HashMap<String, Integer> map = new HashMap<String, Integer>();
	TreeMap<String, Integer> tree = new TreeMap<String,Integer>();
	String buffer[];
	String forBuffer[];
	int bufferCounter = 0;
	BufferedReader buffReader;
	
	boolean loopMode;
	
	String valueKey;
	int loopCounter;
	int loopMax;

	public static void main (String[] args) {
		if(args.length >= 1){
			long startTime = System.currentTimeMillis();
			Zplusminus interpret =  new Zplusminus();
			interpret.readFile(args[0]);
			long stopTime = System.currentTimeMillis();
		    long elapsedTime = stopTime - startTime;
		    //System.out.println(elapsedTime);
		}
	}
	
	protected void readFile(String fileName){
		try {
			loopMode = false;
			buffReader =  new BufferedReader(new FileReader(fileName));
			//System.out.println("file found!");  for testing purposes.
			startLine();
			
		} catch (FileNotFoundException e) {
			System.out.println("File not found, terminating.");
		}
	}
	
	protected void printVals(){
		//tree
		//System.out.println("Printing Values...");
		java.util.Iterator<String> it = tree.descendingKeySet().iterator();
		printValueRec(it);
	}
	
	private void printValueRec(java.util.Iterator<String> it){
		if( it.hasNext()){
			String key = it.next();
			printValueRec(it);
			System.out.println(key + "=" + tree.get(key));
		}
	}
	
	protected void startLine(){
		switch(interpretLine()){
		case END:
			printVals();
			break;
		case CHECKSEMICOLON:
			try {
				getWord();
			} catch (IOException e) {
				break;
			}
		case FOREGOSEMICOLON:
			if(loopMode && (buffer.length <= bufferCounter)){
				loopCounter++;
				if(loopCounter < loopMax){
					buffer = forBuffer.clone();
					bufferCounter = 0;
				}else{
					loopMode = false;
					//System.out.println("End Loop mode.");
				}
			}
			startLine();
			break;
		default:
			//System.out.println("MAJOR ERROR");
		}
	}
	
	protected int interpretLine(){
		int codeVal = 100;
		try {
			String key = getWord();
			if(key != null){
				switch (findKeyword(key)){
				case -1:
					interpretOperator(key);
					codeVal = CHECKSEMICOLON;
					break;
				case DEF:
					tree.put(getWord(), 0);
					codeVal = CHECKSEMICOLON;
					break;
				case FOR:
					//System.out.println("Entering for loop");
					loopCounter = 0;
					loopMax = Integer.parseInt(getWord());
					String set = getWord();
					String holder = "";
					while(!set.equals("ENDFOR")){
						holder += set;
						holder += " ";
						set = getWord();
					}
					forBuffer = holder.split(" ");
					buffer = forBuffer.clone();
					bufferCounter = 0;
					loopMode = true;
					codeVal = FOREGOSEMICOLON;
					break;
				}
			}else{
				codeVal = END;
			}
		} catch (IOException e) {
			codeVal = END;
		}
		return codeVal;
	}
	
	protected void interpretOperator(String key) throws IOException{
		int op = findOperator(getWord());
		String operand = getWord();
		int opVal1, opVal2;
		if(tree.containsKey(operand)){
			opVal2 = tree.get(operand);
		}else{
			opVal2 = Integer.parseInt(operand);
		}
		switch(op){
		case PLUS:
			opVal1 = tree.remove(key);
			//System.out.println(key + " = "  + opVal1 + "   " + key + " = " + opVal1 + " + " + opVal2);
			tree.put(key, opVal1 + opVal2);
			break;
		case TIMES:
			opVal1 = tree.remove(key);
			//System.out.println(key + " = "  + opVal1 + "   " + key + " = " + opVal1 + " * " + opVal2);
			tree.put(key, opVal1 * opVal2);
			break;
		case EQUALS:
			tree.remove(key);
			tree.put(key, opVal2);
		}
	}
	
	protected String getWord() throws IOException{
		if( (buffer == null) || (buffer.length <= bufferCounter)){
			String rawString = buffReader.readLine();
			if(rawString == null){
				return rawString; 
			}
			buffer = rawString.split(" ");
			bufferCounter = 0;
			return getWord();
		} else {
			String returnVal = buffer[bufferCounter];
			bufferCounter++;
			if(returnVal.equals("")){
				return getWord();
			}
			return returnVal;
		}
	}
	
	/**
	 * Checks whether a string is a keyword and returns a corresponding 
	 * int identifier.  -1 means not a keyword
	 * @param term The string to be checked
	 * @return
	 */
	protected int findKeyword(String term){ 
		int val = -1;
		for(int x = 0;  x < keyWords.length; x++){
			if(term.equals(keyWords[x])){
				val = x;
				x = keyWords.length;
			}
		}
		return val;
	}
	
	protected int findOperator(String operator){
		int val = -1;
		for(int x = 0; x < operators.length; x++){
			if(operator.equals( operators[x])){
				val = x;
				x = operators.length;
			}
		}
		return val;
	}
}
