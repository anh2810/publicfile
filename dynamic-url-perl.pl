#!/usr/bin/perl
	my $uri = 'https://ipv4.cloudns.net/api/dynamicURL/?q=NzM4OTk0Njo1MDYxMDk1NzY6Yzk3ZGFhNmJjMGYzZjk1MDQ2M2RiMWQ2NjFiYjIxODE3ZTVhYmZhMGY1YWNiZDk0MDY1NGU5OWUxNzQxNjE4Ng';

	use HTTP::Tiny;
	eval { HTTP::Tiny->can_ssl }
	or die "Please ensure you have HTTP::Tiny (>= 0.055) and IO::Socket::SSL";
	my $res = HTTP::Tiny->new()->get($uri);
	$res->{success} or die "$res->{status} $res->{reason}";
	print {*STDERR} "notification sent successfully" if $ENV{DEBUG};