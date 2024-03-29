function Get-RandomBytes {
    param(
        [int] $Count
    )

    if ($Count -lt 1) {
        throw "Count must be a positive integer greater than 0."
    }

    $RandomBytes = @()

    for ($i = 0; $i -lt $Count; $i++) {
        $RandomBytes += Get-Random -Minimum 0 -Maximum 255
    }

    return $RandomBytes
}

function RandomIPv4 {
    [IPAddress]::Parse([String](Get-Random))
}

function TcpSendRecv {
    param(
        [int] $Port = 5005,
        $IP = "127.0.0.1",
        $Message =( Get-RandomBytes -Count 100)
    )

    # Get a random IP address
    $Address = RandomIPv4
    $target=[system.net.IPAddress]::Parse($IP)
    # Create IP Endpoint
    $End = New-Object System.Net.IPEndPoint $target, $Port

    # Create Socket
    $Saddrf   = [System.Net.Sockets.AddressFamily]::InterNetwork
    $Stype    = [System.Net.Sockets.SocketType]::Stream
    $Ptype    = [System.Net.Sockets.ProtocolType]::Tcp  # Tcp or Udp
    $Sock     = New-Object System.Net.Sockets.Socket $saddrf, $stype, $ptype
    #$Sock.TTL = 26

    try {
        # Connect to socket
        $Sock.Connect($End)

        # Create encoded buffer
        $Enc     = [System.Text.Encoding]::ASCII
        $Buffer  = $Enc.GetBytes($Message)

        # Send the buffer
        $Sent   = $Sock.Send($Buffer)
        "{0} characters sent to: {1} " -f $Sent,$IP
        "Message is:`n$Message"

      <#  # Edit this line if you want to Get response on TCP Assuming receive buffer is 400
        $buffer = New-Object System.Byte[] 400
        $Received = $Sock.Receive($buffer)   # Overflow Exploit!
        "Received $Received bytes"

        if ($Received -ne 0) {
            $Encode = New-Object "System.Text.ASCIIEncoding"
            $msg = $Encode.GetString($buffer)
            "TCP Message received: $msg"
        }
        #>
    }
    catch {
        Write-Host "Error occurred: $_"
    }
    finally {
        # Close the socket
   #     $Sock.Shutdown([System.Net.Sockets.SocketShutdown]::Both)
        $Sock.Close()
    }
}

# Call the function 
TcpSendRecv 
