package matrix;

public class UpperTriangleMatrix extends SquareMatrix {

	public UpperTriangleMatrix(double[][] val) {
		super(val);
		this.matrix=val;
		if(!isUpperTriangle(val)) {System.err.println("NOT ColMatrix!");System.exit(1);}
	}
	@Override
	public LowerTriangleMatrix transpose() {
		double[][] transposed=super.transpose().getValues();
		 return new LowerTriangleMatrix(transposed);
		
	}
}
