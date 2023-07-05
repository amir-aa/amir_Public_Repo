package matrix;

public class ConcreteMatrix extends AbstractMatrix {

	public  int getRows() {
		return this.matrix.length;
		
	}
	protected void sameDimensions(AbstractMatrix other) {
		
		
	}
	
			@Override
			public matrix.AbstractMatrix subtract(matrix.AbstractMatrix other) {
				double[][] matrix1=this.matrix;
				double[][] matrix2=other.matrix;
				int r=matrix1.length;
			    int c=matrix1[0].length;
				double[][] result=new double[r][c];
				ConcreteMatrix newm=new ConcreteMatrix();
			    for (int i=0;i<r;i++) {
			        for (int j=0;j<c;j++) {
			            result[i][j]=matrix1[i][j]-matrix2[i][j];
			        }
			    }
			    newm.matrix=result;
				return newm;
			}
			@Override
			public matrix.AbstractMatrix add(matrix.AbstractMatrix other) {
				
				double[][] matrix1=this.matrix;
				double[][] matrix2=other.matrix;
				int r=matrix1.length;
			    int c=matrix1[0].length;
				double[][] result=new double[r][c];
				ConcreteMatrix newm=new ConcreteMatrix();
			    for (int i=0;i<r;i++) {
			        for (int j=0;j<c;j++) {
			            result[i][j]=matrix1[i][j]+matrix2[i][j];
			        }
			    }
			    newm.matrix=result;
				return newm;
			}
			@Override
			public double[] getColumns() {
				// TODO Auto-generated method stub
				return 0;
			}
			@Override
			public double[] getValues() {
				// TODO Auto-generated method stub
				return null;
			}
			@Override
			public double getValues(int i, int j) {
				// TODO Auto-generated method stub
				return this.matrix[i][j];
			}
			@Override
			protected void sameDimensionsForMultiplication(AbstractMatrix other) {
				// TODO Auto-generated method stub
				
			}
			@Override
			public void print() {
				// TODO Auto-generated method stub
				
			}
			@Override
			public AbstractMatrix multiplyFromLeft(AbstractMatrix other) {
				// TODO Auto-generated method stub
				return null;
			}
			@Override
			public AbstractMatrix multiplyByScalar(AbstractMatrix scalar) {
				// TODO Auto-generated method stub
				return null;
			}
			@Override
			public AbstractMatrix transpose() {
				int rows = getRows();
		        int cols = getColumns();
		        double[][] transposedValues = new double[cols][rows];

		        for (int i =0;i<rows;i++) {
		            for (int j=0;j<cols;j++) {
		                transposedValues[j][i] = getValues(i, j);
		            }
		        }
		        ConcreteMatrix newcm=new ConcreteMatrix();
		        newcm.matrix=transposedValues;//assign transposed to new object
		        return newcm;
				
			}
		};


		
	
				

class RowMatrix extends ConcreteMatrix{}
class ColumnMatrix extends ConcreteMatrix{}
class SquareMatrix extends ConcreteMatrix{}
