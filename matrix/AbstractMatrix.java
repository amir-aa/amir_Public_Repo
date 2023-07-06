package matrix;
import java.util.*;
public abstract class AbstractMatrix {
	protected static double matrix[][];
	public abstract int getRows();
	public abstract int getColumns();
	public abstract double[][] getValues();
	public abstract double getValue(int i,int j);
	protected abstract void sameDimensions(AbstractMatrix other);
	protected abstract void sameDimensionsForMultiplication(AbstractMatrix other);
	public abstract void print();
	protected static boolean isDiagonal() {
		if (matrix.length != matrix[0].length) {return false;}//must be a square
        for (int i=0; i<matrix.length;i++) {
            for (int j=0;j< matrix[0].length;j++) {
                if (i!=j && matrix[i][j]!=0) {return false;}
            }
        }	
		return true;
	}
	
	protected static boolean isIdentity(double[][] matrix) {
		if (matrix.length != matrix[0].length) {return false;}//must be a square
        for (int i=0; i<matrix.length;i++) {if(matrix[i][i]!=1) {return false;} }	
		return true;
	}
	protected static boolean isUpperTriangle(double[][] matrix) {
		for (int i=1;i<matrix.length;i++) {
            for (int j=0;j<i;j++) {
                if (matrix[i][j]!=0) {return false;}
            }
        }
		return true;	
	}
	
	protected static boolean isLowerTriangle(double[][] matrix)
	{
		for (int i=1;i<matrix.length;i++) {
            for (int j=matrix[0].length;j>i;j--) {
                if(matrix[i][j]!=0) {return false;}
            }
        }
		return true;
	}
   /* protected AbstractMatrix checkProperty(double[][] values) {
    	this.matrix=values;
        if (isIdentity(values)) {
            return new IdentityMatrix(values);
        } else if (isDiagonal()) {
            return new DiagonalMatrix(values);
        } else if (isUpperTriangle(values)) {
            return new UpperTriangleMatrix(values);
        }
        return null;
    }*/
	public abstract AbstractMatrix multiplyFromLeft(AbstractMatrix other);
	public abstract AbstractMatrix multiplyByScalar(AbstractMatrix scalar);
	public abstract AbstractMatrix add(AbstractMatrix other);
	public abstract AbstractMatrix subtract(AbstractMatrix other);
	public abstract AbstractMatrix transpose();
	
		

}
