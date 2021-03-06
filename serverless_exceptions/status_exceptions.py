# -*- coding: utf-8 -*-

class ServerlessHTTPException(Exception):
    """
        Baseclass for all HTTP exceptions.  This exception can be called in AWS Lambda
        for triggering API Status Codes
        """

    code = None
    description = None

    def __init__(self, description=None, response=None):
        if description is not None:
            self.description = description
        self.response = response
        message = "[%s]%s" % (self.code, self.description)
        Exception.__init__(self, message)



class BadRequest(ServerlessHTTPException):
    """*400* `Bad Request`

    Raise if the browser sends something to the application the application
    or server cannot handle.
    """
    code = 400
    description = (
        'The browser (or proxy) sent a request that this server could '
        'not understand.'
    )


class Unauthorized(ServerlessHTTPException):
    """*401* `Unauthorized`

    Raise if the user is not authorized.  Also used if you want to use HTTP
    basic auth.
    """
    code = 401
    description = (
        'The server could not verify that you are authorized to access '
        'the URL requested.  You either supplied the wrong credentials (e.g. '
        'a bad password), or your browser doesn\'t understand how to supply '
        'the credentials required.'
    )


class Forbidden(ServerlessHTTPException):
    """*403* `Forbidden`

    Raise if the user doesn't have the permission for the requested resource
    but was authenticated.
    """
    code = 403
    description = (
        'You don\'t have the permission to access the requested resource. '
        'It is either read-protected or not readable by the server.'
    )


class NotFound(ServerlessHTTPException):
    """*404* `Not Found`

    Raise if a resource does not exist and never existed.
    """
    code = 404
    description = (
        'The requested URL was not found on the server.  '
        'If you entered the URL manually please check your spelling and '
        'try again.'
    )


class MethodNotAllowed(ServerlessHTTPException):
    """*405* `Method Not Allowed`

    Raise if the server used a method the resource does not handle.  For
    example `POST` if the resource is view only.  Especially useful for REST.

    The first argument for this exception should be a list of allowed methods.
    Strictly speaking the response would be invalid if you don't provide valid
    methods in the header which you can do with that list.
    """
    code = 405
    description = 'The method is not allowed for the requested URL.'


class NotAcceptable(ServerlessHTTPException):
    """*406* `Not Acceptable`

    Raise if the server can't return any content conforming to the
    `Accept` headers of the client.
    """
    code = 406

    description = (
        'The resource identified by the request is only capable of '
        'generating response entities which have content characteristics '
        'not acceptable according to the accept headers sent in the '
        'request.'
    )


class RequestTimeout(ServerlessHTTPException):
    """*408* `Request Timeout`

    Raise to signalize a timeout.
    """
    code = 408
    description = (
        'The server closed the network connection because the browser '
        'didn\'t finish the request within the specified time.'
    )


class Conflict(ServerlessHTTPException):
    """*409* `Conflict`

    Raise to signal that a request cannot be completed because it conflicts
    with the current state on the server.

    .. versionadded:: 0.7
    """
    code = 409
    description = (
        'A conflict happened while processing the request.  The resource '
        'might have been modified while the request was being processed.'
    )


class Gone(ServerlessHTTPException):
    """*410* `Gone`

    Raise if a resource existed previously and went away without new location.
    """
    code = 410
    description = (
        'The requested URL is no longer available on this server and there '
        'is no forwarding address. If you followed a link from a foreign '
        'page, please contact the author of this page.'
    )


class LengthRequired(ServerlessHTTPException):
    """*411* `Length Required`

    Raise if the browser submitted data but no ``Content-Length`` header which
    is required for the kind of processing the server does.
    """
    code = 411
    description = (
        'A request with this method requires a valid <code>Content-'
        'Length</code> header.'
    )


class PreconditionFailed(ServerlessHTTPException):
    """*412* `Precondition Failed`

    Status code used in combination with ``If-Match``, ``If-None-Match``, or
    ``If-Unmodified-Since``.
    """
    code = 412
    description = (
        'The precondition on the request for the URL failed positive '
        'evaluation.'
    )


class RequestEntityTooLarge(ServerlessHTTPException):
    """*413* `Request Entity Too Large`

    The status code one should return if the data submitted exceeded a given
    limit.
    """
    code = 413
    description = (
        'The data value transmitted exceeds the capacity limit.'
    )


class RequestURITooLarge(ServerlessHTTPException):
    """*414* `Request URI Too Large`

    Like *413* but for too long URLs.
    """
    code = 414
    description = (
        'The length of the requested URL exceeds the capacity limit '
        'for this server.  The request cannot be processed.'
    )


class UnsupportedMediaType(ServerlessHTTPException):
    """*415* `Unsupported Media Type`

    The status code returned if the server is unable to handle the media type
    the client transmitted.
    """
    code = 415
    description = (
        'The server does not support the media type transmitted in '
        'the request.'
    )


class RequestedRangeNotSatisfiable(ServerlessHTTPException):
    """*416* `Requested Range Not Satisfiable`

    The client asked for a part of the file that lies beyond the end
    of the file.

    .. versionadded:: 0.7
    """
    code = 416
    description = (
        'The server cannot provide the requested range.'
    )


class ExpectationFailed(ServerlessHTTPException):
    """*417* `Expectation Failed`

    The server cannot meet the requirements of the Expect request-header.

    .. versionadded:: 0.7
    """
    code = 417
    description = (
        'The server could not meet the requirements of the Expect header'
    )


class ImATeapot(ServerlessHTTPException):
    """*418* `I'm a teapot`

    The server should return this if it is a teapot and someone attempted
    to brew coffee with it.

    .. versionadded:: 0.7
    """
    code = 418
    description = (
        'This server is a teapot, not a coffee machine'
    )


class UnprocessableEntity(ServerlessHTTPException):
    """*422* `Unprocessable Entity`

    Used if the request is well formed, but the instructions are otherwise
    incorrect.
    """
    code = 422
    description = (
        'The request was well-formed but was unable to be followed '
        'due to semantic errors.'
    )


class PreconditionRequired(ServerlessHTTPException):
    """*428* `Precondition Required`

    The server requires this request to be conditional, typically to prevent
    the lost update problem, which is a race condition between two or more
    clients attempting to update a resource through PUT or DELETE. By requiring
    each client to include a conditional header ("If-Match" or "If-Unmodified-
    Since") with the proper value retained from a recent GET request, the
    server ensures that each client has at least seen the previous revision of
    the resource.
    """
    code = 428
    description = (
        'This request is required to be conditional; try using "If-Match" '
        'or "If-Unmodified-Since".'
    )


class TooManyRequests(ServerlessHTTPException):
    """*429* `Too Many Requests`

    The server is limiting the rate at which this user receives responses, and
    this request exceeds that rate. (The server may use any convenient method
    to identify users and their request rates). The server may include a
    "Retry-After" header to indicate how long the user should wait before
    retrying.
    """
    code = 429
    description = (
        'This user has exceeded an allotted request count. Try again later.'
    )


class RequestHeaderFieldsTooLarge(ServerlessHTTPException):
    """*431* `Request Header Fields Too Large`

    The server refuses to process the request because the header fields are too
    large. One or more individual fields may be too large, or the set of all
    headers is too large.
    """
    code = 431
    description = (
        'One or more header fields exceeds the maximum size.'
    )


class InternalServerError(ServerlessHTTPException):
    """*500* `Internal Server Error`

    Raise if an internal server error occurred.  This is a good fallback if an
    unknown error occurred in the dispatcher.
    """
    code = 500
    description = (
        'The server encountered an internal error and was unable to '
        'complete your request.  Either the server is overloaded or there '
        'is an error in the application.'
    )


class NotImplemented(ServerlessHTTPException):
    """*501* `Not Implemented`

    Raise if the application does not support the action requested by the
    browser.
    """
    code = 501
    description = (
        'The server does not support the action requested by the '
        'browser.'
    )


class BadGateway(ServerlessHTTPException):
    """*502* `Bad Gateway`

    If you do proxying in your application you should return this status code
    if you received an invalid response from the upstream server it accessed
    in attempting to fulfill the request.
    """
    code = 502
    description = (
        'The proxy server received an invalid response from an upstream '
        'server.'
    )


class ServiceUnavailable(ServerlessHTTPException):
    """*503* `Service Unavailable`

    Status code you should return if a service is temporarily unavailable.
    """
    code = 503
    description = (
        'The server is temporarily unable to service your request due to '
        'maintenance downtime or capacity problems.  Please try again '
        'later.'
    )


class GatewayTimeout(ServerlessHTTPException):
    """*504* `Gateway Timeout`

    Status code you should return if a connection to an upstream server
    times out.
    """
    code = 504
    description = (
        'The connection to an upstream server timed out.'
    )


class HTTPVersionNotSupported(ServerlessHTTPException):
    """*505* `HTTP Version Not Supported`

    The server does not support the HTTP protocol version used in the request.
    """
    code = 505
    description = (
        'The server does not support the HTTP protocol version used in the '
        'request.'
    )
