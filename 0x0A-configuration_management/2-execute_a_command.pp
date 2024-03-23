#puppet manisfest that kills the process named killmenow
exec { 'kill_killmenow':
        command => '/bin/pkill killmenow',
}