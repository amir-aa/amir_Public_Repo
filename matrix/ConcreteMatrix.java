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
			public int getColumns() {
				return this.matrix[0].length;
			}
			@Override
			public double[][] getValues() {
				
				return this.matrix;
			}
			@Override
			public double getValue(int i, int j) {
				// TODO Auto-generated method stub
				return this.matrix[i][j];
			}
			@Override
			protected void sameDimensionsForMultiplication(AbstractMatrix other) {
				// TODO Auto-generated method stub
				
			}
			@Override
			public void print() {
		       
		        int r=getRows();
		        int c=getColumns();
		        for (int i=0; i<r;i++) {
		            for (int j=0;j<c;j++) {System.out.printf("%.2f ", this.matrix[i][j]);}
		            System.out.println();
		        }
				
			}
			@Override
			public AbstractMatrix multiplyFromLeft(AbstractMatrix other) {
	
			    AbstractMatrix transposedThis=transpose();
			    AbstractMatrix tother=other.transpose();
			    AbstractMatrix result=tother.multiplyFromLeft(transposedThis);
			    return result.transpose();
				
			}
			@Override
			public AbstractMatrix multiplyByScalar(AbstractMatrix scalar) {
				// TODO Auto-generated method stub
				return null;
			}
			@Override
			public AbstractMatrix transpose() {
				int row= getRows();
		        int col= getColumns();
		        double[][] transposedValues = new double[col][row];
		        for(int i =0;i<row;i++) {
		            for(int j=0;j<col;j++) {transposedValues[j][i]=getValue(i, j);}
		        }
		        ConcreteMatrix newcm=new ConcreteMatrix();
		        newcm.matrix=transposedValues;//assign transposed to new object
		        return newcm;
				
			}
		};

	
class ColumnMatrix extends ConcreteMatrix{
	public ColumnMatrix(double val[][]) {
				super();
				this.matrix=val;
				if(getColumns()>1){System.err.println("NOT ColMatrix!");System.exit(1);}
			}
			
			@Override
		    public RowMatrix transpose() {
		        double[][] transposedValues = new double[getColumns()][getRows()];
		        for (int i= 0;i<getRows();i++) {
		            for (int j=0;j<getColumns();j++) {
		                transposedValues[j][i]=getValue(i,j);
		            }
		        }
		        return new RowMatrix(transposedValues);
		    }
		}
	
class RowMatrix extends ConcreteMatrix{
	public RowMatrix(double[][] val) {
        super();
        this.matrix=val;
	//System.out.println(this.getRows());
        if(this.getRows()>1) {
            System.err.println("NOT RowMatrix!");
            System.exit(1);
        }
    }
	@Override
    public ColumnMatrix transpose() {
        double[][] transposedValues = new double[getColumns()][getRows()];

        for (int i=0;i<getRows();i++) {
            for (int j =0;j<getColumns();j++) {
                transposedValues[j][i]=getValue(i,j);
            }
        }

        return new ColumnMatrix(transposedValues);
    }
}


