package matrix;

public class LowerTriangleMatrix extends SquareMatrix{
	public LowerTriangleMatrix(double[][] val) {
		super(val);
		if(!isLowerTriangle(val)) {System.err.println("NOT ColMatrix!");System.exit(1);}
		this.matrix=val;
	}
	@Override
	public UpperTriangleMatrix transpose() {
		double[][] transposed=super.transpose().getValues();
		 return new UpperTriangleMatrix(transposed);
		
	}
}
