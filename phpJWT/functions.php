//append to functions.php belongs to the theme 


define('JWT_SECRET_KEY', 'TEST');

function generate_jwt_token($user_id) {
    $issuedAt = time();
    $expirationTime = $issuedAt + (60 * 60);  // jwt ttl (1h)
    $payload = array(
        'iat' => $issuedAt,
        'exp' => $expirationTime,
        'data' => array(
            'user_id' => $user_id
        )
    );

    return JWT::encode($payload, JWT_SECRET_KEY);
}

function validate_jwt_token($token) {
    try {
        $decoded = JWT::decode($token, JWT_SECRET_KEY);
        return $decoded['data']['user_id'];
    } catch (Exception $e) {
        return null;
    }
}

add_action('rest_api_init', function () {
    register_rest_route('custom/v1','/login', array(
        'methods' => 'POST',
        'callback' => 'custom_login',
    ));

    register_rest_route('custom/v1','/register', array(
        'methods' => 'POST',
        'callback' => 'custom_register',
    ));
});

function custom_login($request) {
    $username = sanitize_text_field($request['username']);
    $password = sanitize_text_field($request['password']);

    $user = wp_authenticate($username, $password);
    if (is_wp_error($user)) { return new WP_Error('invalid_credentials','Invalid username or password', array('status' => 403));}
    $token=generate_jwt_token($user->ID);
    return array(
        'token' => $token,
        'user_id' => $user->ID,
        'username' => $user->user_login,
        'email' => $user->user_email
    );
}

function custom_register($request) {
    $username = sanitize_text_field($request['username']);
    $password = sanitize_text_field($request['password']);
    $email = sanitize_email($request['email']);

    if (username_exists($username) || email_exists($email)) {
        return new WP_Error('user_exists', 'Username or Email already exists', array('status' => 400));
    }

    $user_id = wp_create_user($username, $password, $email);

    if (is_wp_error($user_id)) {
        return new WP_Error('registration_failed', 'User registration failed', array('status' => 500));
    }

    // Optionally, send a welcome email to the user
    wp_new_user_notification($user_id, null, 'user');

    return array(
        'user_id' => $user_id,
        'username' => $username,
        'email' => $email,
    );
}

//-----------------------------jwt-----------------------

function login_user_from_token() {
    if (isset($_GET['token'])) {
        $token = $_GET['token'];
        $user_id = validate_jwt_token($token);

        if ($user_id) {
            wp_set_current_user($user_id);
            wp_set_auth_cookie($user_id);
            wp_redirect(home_url());
            exit;
        }
    }
}
add_action('init', 'login_user_from_token');
