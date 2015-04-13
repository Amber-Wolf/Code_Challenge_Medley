
public class BaseCase {

	public static void main (String[] args) {
		long startTime = System.currentTimeMillis();
		int a, b;
		a = b =0;
		for(int x =0; x<10000; x++){
			a++;
		}
		System.out.println("a = " + a);
		System.out.println("b = " + b);
		long stopTime = System.currentTimeMillis();
	    long elapsedTime = stopTime - startTime;
	    System.out.println(elapsedTime);
	}
}
