<?php

function diffie_hellman($p, $g) {
    // Choose a private key
    $private_key = rand(2, $p - 2);
    $public_key = gmp_powm($g, $private_key, $p);

    return array($private_key, $public_key);
}

function generate_shared_secret($private_key, $other_public_key, $p) {
    // Calculate the shared secret
    $shared_secret = gmp_powm($other_public_key, $private_key, $p);

    return $shared_secret;
}

$p = 23; 
$g = 5;   

// Alice
list($alice_private, $alice_public) = diffie_hellman($p, $g);

// Bob
list($bob_private, $bob_public) = diffie_hellman($p, $g);
$alice_s = generate_shared_secret($alice_private, $bob_public, $p);
$bob_s = generate_shared_secret($bob_private, $alice_public, $p);

echo "Alice's shared secret: $alice_s\n";
echo "Bob's shared secret: $bob_s\n";

?>
