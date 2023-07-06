package matrix;

public class SquareMatrix extends ConcreteMatrix {
	public SquareMatrix(double[][] val) {
		if(val.length!=val[0].length) {System.err.println("it is not SQUARE!");System.exit(1);}
		this.matrix=val;
	}
	
	
	private double determinant(double[][] matrix) {
		
		int d=this.matrix.length;
		if (d==1) {return this.matrix[0][0];}else if (d==2)
		{
	        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0];
	    }
	    double determin=0;
	    for (int j=0;j<d;j++) {
	        double[][] submatrix=new double[d-1][d-1];
	        for (int i = 1; i <d; i++) {
	            int k = 0;
	            for (int col=0;col<d;col++) {
	                if (col!=j) {
	                    submatrix[i-1][k]=matrix[i][col];
	                    k++;
	                }
	            }
	        }
	        determin+=Math.pow(-1,j)*matrix[0][j]*determinant(submatrix);
	    }
	    return determin;
	}
	
	public double determinant() {
		int d=this.matrix.length;
		if (d==1) {return this.matrix[0][0];}else if (d==2)
		{
	        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0];
	    }
	    double determin=0;
	    for (int j=0;j<d;j++) {
	        double[][] submatrix=new double[d-1][d-1];
	        for (int i = 1; i <d; i++) {
	            int k = 0;
	            for (int col=0;col<d;col++) {
	                if (col!=j) {
	                    submatrix[i-1][k]=matrix[i][col];
	                    k++;
	                }
	            }
	        }
	        determin+=Math.pow(-1,j)*matrix[0][j]*determinant(submatrix);
	    }
	    return determin;
		
	}
}
