# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from azure.core import PipelineClient
from azure.core.pipeline import Pipeline
from azure.core.pipeline.policies import ContentDecodePolicy
from azure.core.pipeline.transport import RequestsTransport
from .policies import ARMAutoResourceProviderRegistrationPolicy


class ARMPipelineClient(PipelineClient):
    """A pipeline client designed for ARM explicitly.
    """

    def _build_pipeline(self, config, **kwargs): # pylint: disable=no-self-use
        transport = kwargs.get('transport')
        policies = kwargs.get('policies')

        if policies is None:  # [] is a valid policy list
            policies = [
                ARMAutoResourceProviderRegistrationPolicy(),
                config.headers_policy,
                config.user_agent_policy,
                config.authentication_policy,
                ContentDecodePolicy(),
                config.redirect_policy,
                config.retry_policy,
                config.custom_hook_policy,
                config.logging_policy,
            ]

        if not transport:
            transport = RequestsTransport(**kwargs)

        return Pipeline(
            transport,
            policies
        )
