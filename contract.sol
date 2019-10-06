pragma solidity >=0.4.22 <0.6.0;

contract write {
    mapping(bytes16 => bytes32) public blockindex;
    int public is_equal;
    bytes32 public end_xor;
    bytes32 public filehash;
    bytes32 public current_xor;
    mapping(uint => bytes32) public blockxor;
    bytes32 public finish_xor;
    
    bytes32 public recordtoken;
    
    
    
    function setbatchs(bytes16 [] memory ctoken, bytes32 [] memory dhash, uint len) public{
        for(uint i=0; i<len; i++) {
            bytes16 x=ctoken[i];
            bytes32 y=dhash[i];
            blockindex[x]=y;
        }
        
    }
    
    
    
    
     function set(bytes16 ctoken, bytes32 dhash) public{
        blockindex[ctoken]=dhash;
    }
    
    
    
    function batch_gethash(bytes16 [] memory enfile, uint len, uint blocknum) public{
        bytes32 xor;
        for(uint i=0; i<len; i++) {
            if(i==0){
                xor=  keccak256(abi.encodePacked(enfile[i]));
            }
            else{
                bytes32 hashfileID= keccak256(abi.encodePacked(enfile[i]));
                xor=xor ^ hashfileID;
            }
        }
        blockxor[blocknum]=xor;
        // end_xor=xor;
    }
    
    
     function getlastxor(uint totalnumber) public{
         bytes32 xor;
         
         for(uint i=0; i<=totalnumber; i++) {
             
            if (i==0){
                xor=blockxor[i];
            }
            else{
                 xor=xor ^ blockxor[i];
            } 
         }
         
         finish_xor=xor;
     }
    
    
  
    
    
     function try_whether_equal(bytes16 token) public returns (int current_xor){
        
        if(blockindex[token]==finish_xor)
        {
            is_equal=1;
        }
        else{
            is_equal=0;
        }

    }
    
    
    
    function gettoken(bytes16 token) public view returns (bytes32){
        return blockindex[token];
    }
    
    
    function check_equal_or_not() public view returns (int){
        return is_equal;
    }
    
    
    
    function check_() public view returns (bytes32){
        return finish_xor;
    }
    
    
    
    function equal_or_not(bytes32 recordhash ) public returns (int current_xor){
        
        if(recordhash==finish_xor)
        {
            is_equal=1;
        }
        else{
            is_equal=0;
        }

    }
    
    // function gethash (bytes16 enfile ) public  returns (bytes32){ 
    //     filehash=  keccak256(abi.encodePacked(enfile));
    // }
    
    // function get_filehash() public view returns (bytes32) {
    //     return filehash;
    // }
    
    
    // function computexor(bytes32 last_xor, bytes32 hashfileID) public  returns (bytes32 current_xor){
        
    //     return last_xor ^ hashfileID;
        
    // }
    
    
    //  function computexor(bytes16 enfile , bytes32 last_xor) public returns (bytes32 current_xor){
        
    //     bytes32 hashfileID=  keccak256(abi.encodePacked(enfile));
    //     end_xor=last_xor ^ hashfileID;
        
    // }
    
    
    //  function xor (bytes32 hafile , bytes32 last_xor) public returns (bytes32 current_xor){
        
    //     end_xor=hafile ^ last_xor;
        
        
    // }
 
    function get_computexor()public view returns (bytes32){
        return end_xor;
    }
    
    
    
    //   function equal_or_not(bytes32 recordhash , bytes32 last_xor) public returns (int current_xor){
        
    //     if(recordhash==last_xor)
    //     {
    //         is_equal=1;
    //     }
    //     else{
    //         is_equal=0;
    //     }

    // }
    
   
    
    
    
    
    
    
}
    
    
    // function 
    
    
    
    // function search()
    
    
    
    

    
