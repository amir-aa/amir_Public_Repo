/*
https://ieeexplore.ieee.org/document/1028931
https://en.wikipedia.org/wiki/Cyclic_redundancy_check
*/
public class CRC {
    private static final int POLYNOMIAL=0xEDB88320;//Ethernet standard. Do not Change it!
    
    public static int calculateCRC(byte[] data) { //32bit Plynominal(divisor)
        int crc=0xFFFFFFFF;//assuming that all bits are 1
        for (byte b:data) {
            crc ^= b&0xFF;
            for (int i=0;i<8;i++) {
                if ((crc&1)==1) {
                    crc = (crc>>>1)^ POLYNOMIAL;
                } else {
                  crc>>>=1;
                }
            }
        }
        return crc^0xFFFFFFFF;
    }
    public static void main(String[] args) {
        String input ="CHECK me!";
        byte[] data=input.getBytes();
        int checksum=calculateCRC(data);
        System.out.println("CRC32 checksum:\t"+checksum);
    }
}
